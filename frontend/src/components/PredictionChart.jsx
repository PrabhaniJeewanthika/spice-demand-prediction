import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const PredictionChart = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis dataKey="prediction_date" />

        <YAxis />

        <Tooltip />

        <Line
          type="monotone"
          dataKey="predicted_quantity"
          stroke="#3182CE"
        />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default PredictionChart;