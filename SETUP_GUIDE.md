# Muhammad Sharyar — Portfolio

A premium, modern portfolio website built with Next.js 14 + Tailwind CSS.

## 🚀 Quick Start (Standalone HTML — Zero Setup)

The `index.html` file is a **complete, self-contained portfolio** that works instantly in any browser.
Just open `index.html` — no npm, no Node.js needed.

---

## ⚙️ Next.js Setup Instructions

### 1. Create the Next.js Project

```bash
npx create-next-app@latest sharyar-portfolio --typescript --tailwind --app --no-src-dir
cd sharyar-portfolio
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Replace Files

Copy all provided files into your project:

```
sharyar-portfolio/
├── app/
│   ├── layout.tsx          ← Root layout with SEO meta
│   ├── page.tsx            ← Main page assembling all sections
│   └── globals.css         ← Design tokens, animations, custom CSS
├── components/
│   ├── Navbar.tsx          ← Sticky nav, dark/light toggle, mobile menu
│   ├── Hero.tsx            ← Hero section with typewriter + animated visual
│   ├── About.tsx           ← About section with stats card
│   ├── Skills.tsx          ← Animated skill bars + pill tags
│   ├── Experience.tsx      ← Timeline layout
│   ├── Projects.tsx        ← Project cards grid
│   ├── Education.tsx       ← Education cards
│   ├── Contact.tsx         ← Contact form + WhatsApp button
│   └── Footer.tsx          ← Footer with links
├── public/
│   └── cv.pdf              ← Your CV (add your actual CV file here)
├── tailwind.config.js
├── next.config.js
└── tsconfig.json
```

### 4. Run Development Server

```bash
npm run dev
```
Visit: http://localhost:3000

### 5. Build for Production

```bash
npm run build
npm start
```

### 6. Deploy to Vercel (Recommended — Free)

```bash
npm install -g vercel
vercel
```

Or connect your GitHub repo at: https://vercel.com/new

---

## 🎨 Design System

| Token | Value |
|-------|-------|
| Primary Font | Syne (Display/Headings) |
| Body Font | Outfit |
| Mono Font | JetBrains Mono |
| Accent Color | #63b3ed (Cyan-Blue) |
| Accent 2 | #9f7aea (Violet) |
| Dark BG | #070710 |
| Light BG | #f0f0fa |

---

## ✨ Features

- ✅ Dark / Light mode with localStorage persistence
- ✅ Smooth CSS scroll-triggered reveal animations
- ✅ Animated skill progress bars (triggered on scroll)
- ✅ Typewriter hero text with multiple roles
- ✅ Floating animated hero visual with orbit rings
- ✅ Sticky navbar with active section tracking
- ✅ Mobile-responsive hamburger menu
- ✅ WhatsApp direct contact button
- ✅ Contact form with WhatsApp redirect
- ✅ CV download button
- ✅ Full SEO meta tags (Open Graph, Twitter Card)
- ✅ Back to top button
- ✅ Toast notifications
- ✅ Zero external JS dependencies (pure CSS animations)

---

## 📱 Responsive Breakpoints

- Mobile: < 640px
- Tablet: 640px–768px  
- Desktop: > 900px

---

## 🔧 Customization

### Update Personal Info
Edit the HTML sections or component files for:
- Name, email, phone, location
- Projects descriptions and links
- Skills percentages (data-width attributes)
- Social media links

### Add Real CV PDF
Replace the CV download function with a real PDF:
```javascript
// In index.html, replace downloadCV() body with:
window.open('/cv.pdf', '_blank')
```

### Deploy to PythonAnywhere
Since you already use PythonAnywhere:
1. Upload `index.html` to your PythonAnywhere files
2. Set it as the static file root
3. Your portfolio is live!

---

## 📄 License
MIT — free to use and modify.
