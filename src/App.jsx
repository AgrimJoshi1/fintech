import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import LoanPage from "./pages/LoanPage";
import AnalyticsPage from "./pages/AnalyticsPage";
import InsurancePage from "./pages/InsurancePage";

import Navbar from "./components/Navbar";

import "./index.css";

function App() {

    return (

        <BrowserRouter>

            <div className="app-container">

                <Navbar />

                <Routes>

                    <Route
                        path="/"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/loan"
                        element={<LoanPage />}
                    />

                    <Route
                        path="/analytics"
                        element={<AnalyticsPage />}
                    />

                    <Route
                        path="/insurance"
                        element={<InsurancePage />}
                    />

                </Routes>

            </div>

        </BrowserRouter>
    );
}

export default App;