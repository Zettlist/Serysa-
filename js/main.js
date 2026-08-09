/* ============================================
   SERYSA — Main JavaScript
   Interactividad, animaciones, cotizador
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  // --- Initialize all modules ---
  initHeader();
  initMobileMenu();
  initParticles();
  initScrollAnimations();
  initCounterAnimations();
  initCotizador();
  initContactForm();
  initSmoothScroll();
});

/* ============================================
   HEADER — Scroll behavior
   ============================================ */
function initHeader() {
  const header = document.getElementById('header');
  let lastScroll = 0;

  window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    if (currentScroll > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
  }, { passive: true });
}

/* ============================================
   MOBILE MENU
   ============================================ */
function initMobileMenu() {
  const toggle = document.getElementById('menuToggle');
  const nav = document.getElementById('mainNav');
  const links = nav.querySelectorAll('.nav-links a');

  toggle.addEventListener('click', () => {
    toggle.classList.toggle('active');
    nav.classList.toggle('active');
    document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
  });

  // Close menu on link click
  links.forEach(link => {
    link.addEventListener('click', () => {
      toggle.classList.remove('active');
      nav.classList.remove('active');
      document.body.style.overflow = '';
    });
  });
}

/* ============================================
   PARTICLES BACKGROUND
   ============================================ */
function initParticles() {
  const container = document.getElementById('particles');
  if (!container) return;

  const particleCount = 30;

  for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');

    const size = Math.random() * 4 + 2;
    const left = Math.random() * 100;
    const delay = Math.random() * 15;
    const duration = Math.random() * 15 + 10;
    const opacity = Math.random() * 0.5 + 0.1;

    particle.style.cssText = `
      width: ${size}px;
      height: ${size}px;
      left: ${left}%;
      animation-delay: ${delay}s;
      animation-duration: ${duration}s;
      opacity: ${opacity};
    `;

    container.appendChild(particle);
  }
}

/* ============================================
   SCROLL ANIMATIONS — Intersection Observer
   ============================================ */
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger animation for sibling elements
        const parent = entry.target.parentElement;
        const siblings = parent ? parent.querySelectorAll('.service-card, .advantage-item, .cert-card, .about-card, .trust-item, .client-logo') : [];

        if (siblings.length > 0) {
          const idx = Array.from(siblings).indexOf(entry.target);
          entry.target.style.transitionDelay = `${idx * 0.1}s`;
        }

        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all animated elements
  const animatedElements = document.querySelectorAll(
    '.reveal, .service-card, .advantage-item, .cert-card, .about-card, .trust-item, .client-logo'
  );

  animatedElements.forEach(el => observer.observe(el));
}

/* ============================================
   COUNTER ANIMATIONS
   ============================================ */
function initCounterAnimations() {
  const counters = document.querySelectorAll('[data-count]');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element) {
  const target = parseInt(element.getAttribute('data-count'));
  const duration = 2000; // ms
  const startTime = performance.now();

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);

    // Ease out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(eased * target);

    element.textContent = current.toLocaleString('es-MX') + '+';

    if (progress < 1) {
      requestAnimationFrame(update);
    }
  }

  requestAnimationFrame(update);
}

/* ============================================
   COTIZADOR INTERACTIVO — Price Calculator
   ============================================ */
function initCotizador() {
  const calcBtn = document.getElementById('calcularBtn');
  const priceResult = document.getElementById('priceResult');
  const priceRange = document.getElementById('priceRange');

  if (!calcBtn) return;

  // Price matrix (MXN ranges)
  const prices = {
    insectos: {
      casa_chica: [800, 1500],
      casa_mediana: [1200, 2200],
      casa_grande: [1800, 3500],
      depto: [700, 1300],
      oficina: [1000, 2000],
      restaurante: [1500, 3000],
      bodega: [2500, 5000],
      industria: [5000, 15000]
    },
    roedores: {
      casa_chica: [1000, 2000],
      casa_mediana: [1500, 3000],
      casa_grande: [2500, 4500],
      depto: [900, 1800],
      oficina: [1200, 2500],
      restaurante: [2000, 4000],
      bodega: [3500, 7000],
      industria: [7000, 20000]
    },
    termitas: {
      casa_chica: [3000, 6000],
      casa_mediana: [5000, 10000],
      casa_grande: [8000, 18000],
      depto: [2500, 5000],
      oficina: [4000, 8000],
      restaurante: [5000, 10000],
      bodega: [10000, 25000],
      industria: [20000, 50000]
    },
    chinches: {
      casa_chica: [2000, 4000],
      casa_mediana: [3500, 6000],
      casa_grande: [5000, 10000],
      depto: [1800, 3500],
      oficina: [2500, 5000],
      restaurante: [3000, 6000],
      bodega: [5000, 10000],
      industria: [8000, 20000]
    },
    aves: {
      casa_chica: [1500, 3000],
      casa_mediana: [2500, 5000],
      casa_grande: [4000, 8000],
      depto: [1200, 2500],
      oficina: [2000, 4000],
      restaurante: [3000, 6000],
      bodega: [5000, 12000],
      industria: [10000, 30000]
    },
    vectores: {
      casa_chica: [900, 1800],
      casa_mediana: [1400, 2800],
      casa_grande: [2200, 4000],
      depto: [800, 1600],
      oficina: [1200, 2500],
      restaurante: [2000, 3500],
      bodega: [3000, 6000],
      industria: [6000, 18000]
    },
    abejas: {
      casa_chica: [1500, 3000],
      casa_mediana: [2000, 4000],
      casa_grande: [3000, 6000],
      depto: [1500, 3000],
      oficina: [2000, 4000],
      restaurante: [2500, 5000],
      bodega: [3000, 6000],
      industria: [5000, 12000]
    },
    fumigacion: {
      casa_chica: [3000, 5000],
      casa_mediana: [4500, 8000],
      casa_grande: [6000, 12000],
      depto: [2500, 4500],
      oficina: [3500, 7000],
      restaurante: [4000, 8000],
      bodega: [8000, 20000],
      industria: [15000, 50000]
    }
  };

  calcBtn.addEventListener('click', () => {
    const plaga = document.getElementById('plagaType').value;
    const space = document.getElementById('spaceType').value;

    if (!plaga || !space) {
      // Shake animation
      calcBtn.style.animation = 'shake 0.5s ease';
      setTimeout(() => calcBtn.style.animation = '', 500);

      if (!plaga) document.getElementById('plagaType').focus();
      else document.getElementById('spaceType').focus();
      return;
    }

    const range = prices[plaga]?.[space];
    if (range) {
      priceRange.textContent = `$${range[0].toLocaleString('es-MX')} — $${range[1].toLocaleString('es-MX')} MXN`;
      priceResult.classList.add('show');

      // Smooth scroll to result
      priceResult.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  });
}

/* ============================================
   CONTACT FORM
   ============================================ */
function initContactForm() {
  const form = document.getElementById('contactForm');
  const success = document.getElementById('formSuccess');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('contactName').value.trim();
    const phone = document.getElementById('contactPhone').value.trim();
    const plaga = document.getElementById('contactPlaga').value;
    const municipio = document.getElementById('contactMunicipio').value;

    if (!name || !phone) {
      return;
    }

    // Build WhatsApp message
    const message = `¡Hola SERYSA! 👋%0A%0A` +
      `Solicito una cotización:%0A` +
      `• Nombre: ${encodeURIComponent(name)}%0A` +
      `• Teléfono: ${encodeURIComponent(phone)}%0A` +
      (plaga ? `• Plaga: ${encodeURIComponent(plaga)}%0A` : '') +
      (municipio ? `• Municipio: ${encodeURIComponent(municipio)}%0A` : '') +
      `%0AGracias.`;

    // Open WhatsApp with pre-filled message
    window.open(`https://wa.me/528112345678?text=${message}`, '_blank');

    // Show success message
    form.style.display = 'none';
    success.classList.add('show');

    // Reset after 5 seconds
    setTimeout(() => {
      form.style.display = '';
      form.reset();
      success.classList.remove('show');
    }, 5000);
  });
}

/* ============================================
   SMOOTH SCROLL
   ============================================ */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;

      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
}

/* ============================================
   SHAKE ANIMATION (for validation feedback)
   ============================================ */
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-8px); }
    50% { transform: translateX(8px); }
    75% { transform: translateX(-4px); }
  }
`;
document.head.appendChild(shakeStyle);
