import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

interface Props {
  currencies: {
    code: string;
    country: string;
    rate: number;
  }[];
}

export default function TopCurrenciesChart({ currencies }: Props) {
  const data = {
    labels: currencies.map(c => c.code),
    datasets: [
      {
        label: 'Exchange Rate to INR',
        data: currencies.map(c => c.rate),
        backgroundColor: 'rgba(255, 107, 107, 0.8)',
        borderColor: 'rgba(255, 217, 61, 1)',
        borderWidth: 2,
        borderRadius: 8,
        hoverBackgroundColor: 'rgba(255, 107, 107, 1)',
        hoverBorderColor: 'rgba(255, 217, 61, 1)',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const,
        labels: {
          font: {
            size: 14,
            weight: '600' as const,
          },
          color: 'rgba(255, 107, 107, 1)',
        },
      },
      tooltip: {
        backgroundColor: 'rgba(255, 107, 107, 0.9)',
        titleColor: 'white',
        bodyColor: 'white',
        padding: 12,
        titleFont: {
          size: 14,
          weight: '600' as const,
        },
        bodyFont: {
          size: 13,
        },
        displayColors: false,
        borderColor: 'rgba(255, 217, 61, 0.5)',
        borderWidth: 1,
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: {
          color: 'rgba(255, 107, 107, 0.1)',
        },
        ticks: {
          font: {
            size: 12,
          },
          color: 'rgba(255, 107, 107, 0.8)',
        },
      },
      x: {
        grid: {
          display: false,
        },
        ticks: {
          font: {
            size: 12,
          },
          color: 'rgba(255, 107, 107, 0.8)',
        },
      },
    },
    animation: {
      duration: 2000,
      easing: 'easeInOutQuart',
    },
    hover: {
      mode: 'nearest',
      intersect: true,
      animationDuration: 200,
    },
  };

  return (
    <div style={{ width: '100%', height: '400px' }}>
      <Bar data={data} options={options} />
    </div>
  );
}