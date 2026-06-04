import { useEffect, useState } from "react";
import {
  Container,
  Heading,
  VStack,
} from "@chakra-ui/react";

import API from "../services/api";
import SummaryCards from "../components/SummaryCards";
import PredictionChart from "../components/PredictionChart";
import PredictionTable from "../components/PredictionTable";

const DemandPrediction = () => {
  const [predictions, setPredictions] = useState([]);
  const [summary, setSummary] = useState({
    total_predictions: 0,
    average_prediction: 0,
  });

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const predictionRes =
      await API.get("predictions/");

    setPredictions(predictionRes.data);

    const summaryRes =
      await API.get("dashboard-summary/");

    setSummary(summaryRes.data);
  };

  return (
    <Container maxW="container.xl" py={10}>
      <VStack spacing={8}>
        <Heading>
          Demand Prediction Dashboard
        </Heading>

        <SummaryCards
          total={summary.total_predictions}
          average={summary.average_prediction}
        />

        <PredictionChart
          data={predictions}
        />

        <PredictionTable
          data={predictions}
        />
      </VStack>
    </Container>
  );
};

export default DemandPrediction;