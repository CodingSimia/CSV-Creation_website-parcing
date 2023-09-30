// @ts-check
const { test, expect } = require('@playwright/test');

test('Find the users data', async ({ page }) => {
  await page.goto('https://www.theagencyre.com/agents?offices=1');

  let previousHeight = 0;
  let currentHeight = await page.evaluate(() => document.body.scrollHeight);

  // Keep scrolling until no more content is loaded
  while (previousHeight < currentHeight) {
    // Scroll to the bottom of the page
    await page.evaluate(() => {
      window.scrollTo(0, document.body.scrollHeight);
    });

    // Wait for a brief moment to let new content load (you can adjust the timeout)
    await page.waitForTimeout(1000);

    // Update height values
    previousHeight = currentHeight;
    currentHeight = await page.evaluate(() => document.body.scrollHeight);
  }

  // Use Playwright to interact with the page
  const employeeCards = await page.$$('.employee-card');
  const userData = [];

  for (const card of employeeCards) {
    const textContent = await card.textContent();
    const [name, sername, email, ...phone] = textContent.split(' ').filter(Boolean);

    // Store user data as an object
    userData.push({
      name: `${name} ${sername}`,
      email,
      phone: phone.join(' '),
    });
  }

  // Now you can log the extracted data to the console
  console.log(userData);

  // You might want to add assertions here using the 'expect' function
  // For example:
  expect(userData.length).toBeGreaterThan(0);
});
