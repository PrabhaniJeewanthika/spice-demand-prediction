import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
} from "@chakra-ui/react";

const PredictionTable = ({ data }) => {
  return (
    <Table variant="simple">
      <Thead>
        <Tr>
          <Th>Date</Th>
          <Th>Product</Th>
          <Th>Predicted Quantity</Th>
        </Tr>
      </Thead>

      <Tbody>
        {data.map((item) => (
          <Tr key={item.id}>
            <Td>{item.prediction_date}</Td>
            <Td>{item.product_name}</Td>
            <Td>
              {Number(
                item.predicted_quantity
              ).toFixed(2)}
            </Td>
          </Tr>
        ))}
      </Tbody>
    </Table>
  );
};

export default PredictionTable;