from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 450, 'height': 950})

    page.goto('http://localhost:8080')
    page.wait_for_load_state('networkidle')

    # Start game
    page.click('text=Begin the Transition')
    page.wait_for_timeout(1500)

    # Screenshot 1: Start
    page.screenshot(path='/tmp/full_01_start.png')
    print("1. Start - Year 0")

    def get_meter_value(meter_name):
        """Try to get a meter value from the page"""
        try:
            # Look for the meter percentage text
            meter = page.locator(f'text="{meter_name}"').locator('..').locator('text=/%/')
            if meter.count() > 0:
                text = meter.first.text_content()
                return int(text.replace('%', ''))
        except:
            pass
        return 50  # Default to middle if can't read

    def play_turn_smart():
        """Play one turn with awareness of meter balance"""
        try:
            # Check for game over first
            game_over = page.locator('#game-over-modal:not(.invisible)')
            if game_over.count() > 0:
                return False

            # Try to read solidarity meter to make smart choices
            # Choice A generally boosts solidarity, Choice B boosts productivity
            # For a balanced game, we want to keep solidarity above ~40

            # Simple heuristic: favor choice A (solidarity) 60% of the time in later game
            import random
            choice = '#choice-a-div' if random.random() < 0.55 else '#choice-b-div'

            choice_el = page.locator(choice)
            if choice_el.is_visible(timeout=1000):
                choice_el.click()
                page.wait_for_timeout(800)
                # Dismiss feedback
                feedback = page.locator('#feedback-splash')
                if feedback.is_visible(timeout=1000):
                    feedback.click()
                    page.wait_for_timeout(200)
            return True
        except Exception as e:
            print(f"  Turn issue: {e}")
            return False

    def play_turns(count):
        """Play multiple turns"""
        for i in range(count):
            if not play_turn_smart():
                return False
        return True

    # Play through all eras
    print("Playing Traditional era (years 0-24)...")
    if not play_turns(24):
        page.screenshot(path='/tmp/full_02_failed.png')
        print("2. FAILED in Traditional era")
    else:
        page.screenshot(path='/tmp/full_02_traditional_end.png')
        print("2. Completed Traditional era")

        game_over = page.locator('#game-over-modal:not(.invisible)')
        if game_over.count() > 0:
            page.screenshot(path='/tmp/full_03_transition_fail.png')
            print("3. Failed transition check")
        else:
            print("Playing Transitional era (years 25-49)...")
            if not play_turns(25):
                page.screenshot(path='/tmp/full_03_failed.png')
                print("3. FAILED in Transitional era")
            else:
                page.screenshot(path='/tmp/full_03_transitional_end.png')
                print("3. Completed Transitional era")

                game_over = page.locator('#game-over-modal:not(.invisible)')
                if game_over.count() > 0:
                    page.screenshot(path='/tmp/full_04_transition_fail.png')
                    print("4. Failed transition check")
                else:
                    print("Playing Modern era (years 50-75)...")
                    if not play_turns(26):
                        page.screenshot(path='/tmp/full_04_failed.png')
                        print("4. FAILED in Modern era")
                    else:
                        page.screenshot(path='/tmp/full_04_end.png')
                        print("4. Reached end of game!")

                        game_over = page.locator('#game-over-modal:not(.invisible)')
                        if game_over.count() > 0:
                            page.screenshot(path='/tmp/full_05_result.png')
                            # Check if it's a win or loss
                            win_text = page.locator('text="Organic Solidarity Achieved"')
                            if win_text.count() > 0:
                                print("5. *** VICTORY! ***")
                            else:
                                print("5. Final result (see screenshot)")

    browser.close()
    print("\nTest complete! Check /tmp/full_*.png")
