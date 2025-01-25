import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import type { CurrencyData } from '../data/currencyData';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

interface Props {
  data: CurrencyData;
}

export default function CurrencyChart({ data }: Props) {
  const chartData = {
    labels: data.historicalData.map(item => item.date),
    datasets: [
      {
        label: `${data.currency} to INR`,
        data: data.historicalData.map(item => item.value),
        borderColor: '#2563eb',
        backgroundColor: 'rgba(37, 99, 235, 0.1)',
        tension: 0.4,
        fill: true,
        pointRadius: 4,
        pointBackgroundColor: '#2563eb',
        pointBorderColor: '#ffffff',
        pointBorderWidth: 2,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top' as const,
        labels: {
          font: {
            size: 12,
            weight: '600' as const,
          },
        },
      },
      title: {
        display: true,
        text: `${data.currency} Historical Trend`,
        font: {
          size: 16,
          weight: '600' as const,
        },
        padding: {
          bottom: 20,
        },
      },
      tooltip: {
        backgroundColor: 'rgba(17, 24, 39, 0.9)',
        padding: 12,
        titleFont: {
          size: 14,
          weight: '600' as const,
        },
        bodyFont: {
          size: 13,
        },
        displayColors: false,
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        grid: {
          color: 'rgba(0, 0, 0, 0.05)',
        },
        ticks: {
          font: {
            size: 12,
          },
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
        },
      },
    },
    interaction: {
      intersect: false,
      mode: 'index' as const,
    },
  };

  return (
    <div className="chart-container">
      <Line data={chartData} options={options} />
    </div>
  );
}