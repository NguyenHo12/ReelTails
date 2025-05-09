// Form handling
document.addEventListener('DOMContentLoaded', function() {
    // Newsletter form handling
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            handleNewsletterSignup(email);
        });
    }

    // Custom order form handling
    const customOrderForm = document.getElementById('custom-order-form');
    if (customOrderForm) {
        customOrderForm.addEventListener('submit', function(e) {
            e.preventDefault();
            handleCustomOrder(this);
        });
    }
});

// Newsletter signup handler
function handleNewsletterSignup(email) {
    // Here you would typically send this to your backend
    console.log('Newsletter signup:', email);
    alert('Thank you for subscribing to our newsletter!');
}

// Custom order handler
function handleCustomOrder(form) {
    const formData = new FormData(form);
    const orderData = {
        name: formData.get('name'),
        email: formData.get('email'),
        productType: formData.get('product-type'),
        customization: formData.get('customization'),
        photo: formData.get('photo')
    };

    // Here you would typically send this to your backend
    console.log('Custom order:', orderData);
    alert('Thank you for your order! We will contact you shortly with the details.');
    form.reset();
}

// Mobile navigation toggle
const navLinks = document.querySelector('.nav-links');
const hamburger = document.createElement('button');
hamburger.classList.add('hamburger');
hamburger.innerHTML = '☰';
hamburger.setAttribute('aria-label', 'Toggle navigation menu');

const mainNav = document.querySelector('.main-nav');
if (mainNav) {
    mainNav.insertBefore(hamburger, navLinks);

    hamburger.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        this.classList.toggle('active');
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Image lazy loading
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
});

// Form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    let isValid = true;

    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    });

    return isValid;
}

// Add error styles to CSS
const style = document.createElement('style');
style.textContent = `
    .error {
        border-color: #e74c3c !important;
    }
    .hamburger {
        display: none;
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem;
    }
    @media (max-width: 768px) {
        .hamburger {
            display: block;
        }
        .nav-links {
            display: none;
        }
        .nav-links.active {
            display: flex;
        }
    }
`;
document.head.appendChild(style); 