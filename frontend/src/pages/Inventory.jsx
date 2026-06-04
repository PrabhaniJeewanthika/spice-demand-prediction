import { useEffect, useState } from "react";
import API from "../services/api";

function Inventory() {
  const [materials, setMaterials] = useState([]);

  useEffect(() => {
    loadInventory();
  }, []);

  const loadInventory = async () => {
    try {
      const response = await API.get("inventory/");
      setMaterials(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div
      style={{
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>Inventory Dashboard</h1>

      <table
        border="1"
        cellPadding="10"
        style={{
          width: "100%",
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Material Name</th>
            <th>Current Stock</th>
            <th>Minimum Stock</th>
            <th>Unit</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {materials.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>

              <td>{item.material_name}</td>

              <td>{item.current_stock}</td>

              <td>{item.minimum_stock}</td>

              <td>{item.unit}</td>

              <td>
                {item.low_stock ? (
                  <span>
                    ⚠️ Low Stock
                  </span>
                ) : (
                  <span>
                    ✅ Available
                  </span>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Inventory;