from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 450, 'height': 950})

    page.goto('http://localhost:8080')
    page.wait_for_load_state('networkidle')

    # Start game
    page.click('text=Begin the Transition')
    page.wait_for_timeout(1500)

    # Screenshot 1: Start - Traditional era with new progress bar
    page.screenshot(path='/tmp/game_01_start.png')
    print("1. Start - Traditional era (Years 0-24)")

    # Play through traditional era - mix of choices
    for i in range(22):
        try:
            # Alternate choices to see balanced gameplay
            choice = page.locator('#choice-b-div' if i % 2 == 0 else '#choice-a-div')
            if choice.is_visible(timeout=1000):
                choice.click()
                page.wait_for_timeout(1000)
                # Dismiss feedback
                page.click('#feedback-splash', timeout=2000)
                page.wait_for_timeout(200)
        except Exception as e:
            print(f"  Turn {i}: {e}")
            break

    # Screenshot 2: Near year 25 - about to check transition requirements
    page.screenshot(path='/tmp/game_02_near_transition.png')
    print("2. Near year 25 - checking transition requirements")

    # Check if game over (failed transition) or still playing
    game_over = page.locator('#game-over-modal:not(.invisible)')
    if game_over.count() > 0:
        page.screenshot(path='/tmp/game_03_transition_result.png')
        print("3. Transition check complete - see screenshot for result")
    else:
        # Continue into transitional era
        for i in range(10):
            try:
                choice = page.locator('#choice-b-div' if i % 2 == 0 else '#choice-a-div')
                if choice.is_visible(timeout=1000):
                    choice.click()
                    page.wait_for_timeout(1000)
                    page.click('#feedback-splash', timeout=2000)
                    page.wait_for_timeout(200)
            except:
                break
        page.screenshot(path='/tmp/game_03_transitional.png')
        print("3. In Transitional era")

    browser.close()
    print("\nTest complete! Check /tmp/game_*.png")
