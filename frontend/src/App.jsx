import { BrowserRouter, Routes, Route } from "react-router-dom";

import DemandPrediction from "./pages/DemandPrediction";
import Inventory from "./pages/Inventory";

function App() {
return ( <BrowserRouter> <Routes>
<Route
path="/"
element={<DemandPrediction />}
/>

    <Route
      path="/inventory"
      element={<Inventory />}
    />
  </Routes>
</BrowserRouter>


);
}

export default App;
