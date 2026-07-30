# 🌍 GlobalFX

**GlobalFX** is a modern, high-performance web application designed to track, convert, and visualize real-time global currency exchange rates with a focus on the Indian Rupee (INR) and 150+ international currencies. Built with Astro 5, React, Three.js, and Chart.js, it features immersive 3D graphics, dynamic charts, and an automated data pipeline.

---

## ✨ Features

- 💱 **Real-Time Currency Conversion**: Instant two-way conversion between 150+ global currencies with live calculations and currency swapping.
- 📊 **Interactive Data Visualizations**: Top currency comparisons powered by Chart.js and React components.
- 🎨 **Immersive 3D Experience**: Animated 3D background effects rendered with Three.js, GSAP, and Framer Motion for a fluid user experience.
- 🤖 **Automated Exchange Rate Pipeline**: Powered by GitHub Actions and Python scripts (`fetch_currencies.py` / `main.py`) fetching live rates from the exchange rate API every 8 hours.
- ⚡ **Blazing Fast Performance**: Powered by Astro 5 for near-zero runtime JavaScript overhead on static content and fast hydration for interactive UI components.
- 📱 **Fully Responsive Layout**: Styled with modern CSS glassmorphism, gradient accents, and dark aesthetic optimized for all screen sizes.

---

## 🛠️ Tech Stack

- **Framework**: [Astro 5](https://astro.build/)
- **UI Components & Interactive Charts**: [React 18](https://react.dev/), [Chart.js](https://www.chartjs.org/), [react-chartjs-2](https://react-chartjs-2.js.org/)
- **3D & Animation**: [Three.js](https://threejs.org/), [GSAP](https://gsap.com/), [Framer Motion](https://www.framer.com/motion/)
- **Data & Automation Pipeline**: Python 3 (`requests`), GitHub Actions (`update_currency.yml`)
- **TypeScript**: Static typing for data structures and component props

---

## 📁 Project Structure

```text
GlobalFX/
├── .github/
│   └── workflows/
│       ├── codeql.yml             # Security analysis workflow
│       └── update_currency.yml    # Scheduled bot fetching latest rates
├── public/
│   └── currencyData.json          # Publicly accessible JSON rate data
├── src/
│   ├── components/
│   │   ├── Background3D.tsx       # Three.js 3D background animation
│   │   ├── CurrencyCard.astro     # Individual currency rate display card
│   │   ├── CurrencyChart.tsx      # Chart.js currency detail visualizer
│   │   ├── Features.astro         # Feature showcase section
│   │   ├── TopCurrenciesChart.tsx # Chart.js bar graph for top currencies
│   │   └── Welcome.astro          # Welcome hero section component
│   ├── data/
│   │   └── currencyData.ts        # Generated TypeScript exchange rates data
│   ├── layouts/
│   │   └── Layout.astro           # Root site layout & global styles
│   └── pages/
│       ├── index.astro            # Homepage with top currencies & rates
│       ├── converter.astro        # Live currency converter tool page
│       └── all-currencies.astro   # Complete searchable currency catalog
├── fetch_currencies.py            # Python script to update currency rates
├── main.py                        # Alternative rate update & git commit utility
├── astro.config.mjs               # Astro framework configuration
├── package.json                   # Project dependencies and npm scripts
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system:
- **Node.js** (v18.x or higher)
- **npm** (v9.x or higher)
- **Python** (v3.8+ required for rate updates)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PRANAY130/GlobalFX.git
   cd GlobalFX
   ```

2. **Install Node dependencies**:
   ```bash
   npm install
   ```

3. **Run the local development server**:
   ```bash
   npm run dev
   ```
   Open [http://localhost:4321](http://localhost:4321) in your browser to view the application.

---

## ⚙️ Available Scripts

In the project directory, you can run:

- `npm run dev`: Starts the Astro development server.
- `npm run build`: Builds the static site for production deployment in `dist/`.
- `npm run preview`: Previews the production build locally.
- `python fetch_currencies.py`: Manually fetches exchange rates from the API and updates `src/data/currencyData.ts` and `public/currencyData.json`.

---

## 🔄 Automated Data Updates

Exchange rates are kept up-to-date automatically:
- A **GitHub Actions workflow** (`.github/workflows/update_currency.yml`) executes every **8 hours**.
- It runs `fetch_currencies.py` to retrieve live exchange rates, regenerates `currencyData.ts` and `currencyData.json`, and commits updated rate data back into the repository.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).