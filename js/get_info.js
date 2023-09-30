Array.from(document.querySelectorAll('.employee-card'))
  .map(card => {
    const [name, sername, email, ...phone] = card.textContent.split(' ').filter(Boolean)

    return {
      name: `${name} ${sername}`,
      email,
      phone: phone.join(' '),
    };
  });