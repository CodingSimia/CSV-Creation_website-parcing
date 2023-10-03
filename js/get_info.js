Array.from(document.querySelectorAll('.employee-card'))
  .map(card => {
    const [name, username, email, ...phone] = card.textContent.split(' ').filter(Boolean)

    return {
      name: `${name} ${username}`,
      email,
      phone: phone.join(' '),
    };
  });
