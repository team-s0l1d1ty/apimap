function generateNavbar() {
  var pages = [
    { name: 'Home', url: 'index.html' },
    { name: 'Results', url: 'results.html' },
    { name: 'Inventory', url: 'inventory.html' }
  ];

  var nav = document.createElement('nav');

  // Create logo element with multi-line ASCII art
  var logo = document.createElement('pre');
  var asciiArt = `
░█████╗░██████╗░██╗███╗░░░███╗░█████╗░██████╗░  ██████╗░░█████╗░████████╗░█████╗░
██╔══██╗██╔══██╗██║████╗░████║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
███████║██████╔╝██║██╔████╔██║███████║██████╔╝  ██║░░██║███████║░░░██║░░░███████║
██╔══██║██╔═══╝░██║██║╚██╔╝██║██╔══██║██╔═══╝░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
██║░░██║██║░░░░░██║██║░╚═╝░██║██║░░██║██║░░░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
  `;
  logo.textContent = asciiArt;
  nav.appendChild(logo);

  for (var i = 0; i < pages.length; i++) {
    var link = document.createElement('a');
    link.href = pages[i].url;
    link.textContent = pages[i].name;
    nav.appendChild(link);
  }

  document.body.appendChild(nav);
}

generateNavbar();
