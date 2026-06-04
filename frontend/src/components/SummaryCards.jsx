import {
  SimpleGrid,
  Stat,
  StatLabel,
  StatNumber,
  Box,
} from "@chakra-ui/react";

const SummaryCards = ({ total, average }) => {
  return (
    <SimpleGrid columns={2} spacing={6}>
      <Box p={5} shadow="md" borderWidth="1px">
        <Stat>
          <StatLabel>Total Predictions</StatLabel>
          <StatNumber>{total}</StatNumber>
        </Stat>
      </Box>

      <Box p={5} shadow="md" borderWidth="1px">
        <Stat>
          <StatLabel>Average Demand</StatLabel>
          <StatNumber>
            {Number(average || 0).toFixed(2)}
          </StatNumber>
        </Stat>
      </Box>
    </SimpleGrid>
  );
};

export default SummaryCards;