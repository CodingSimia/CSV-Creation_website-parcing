new Promise((resolve) => {
    const scrollInterval = setInterval(() => {
      window.scrollBy(0, 400);
  
      if (window.innerHeight + window.scrollY >= document.body.clientHeight) {
        const data = Array.from(document.querySelectorAll('.employee-card'))
          .map((card) => {
            const [name, sername, email, ...phone] = card.textContent.split(' ').filter(Boolean);
  
            return {
              name: `${name} ${sername}`,
              email,
              phone: phone.join(' '),
            };
          })
        resolve(data)
        clearInterval(scrollInterval);
      }
    }, 500);
  }).then(console.log)