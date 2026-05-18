import { useEffect, useState } from "react";

import { predictLoan } from "../api/loanApi";
import { adjustEMI } from "../api/emiApi";
import { getAnalytics } from "../api/analyticsApi";

function Dashboard() {

    const [loanData, setLoanData] = useState(null);
    const [emiData, setEmiData] = useState(null);
    const [analytics, setAnalytics] = useState(null);

    const userData = {
        income: 50000,
        expenses: 18000,
        missed_payments: 1,
        work_consistency: 0.82,
        daily_income_variation: 0.25
    };

    useEffect(() => {

        async function fetchData() {

            const loan = await predictLoan(userData);
            const emi = await adjustEMI(userData);
            const analyticsData =
                await getAnalytics(userData);

            setLoanData(loan);
            setEmiData(emi);
            setAnalytics(analyticsData);
        }

        fetchData();

    }, []);

    return (
        <div style={{ padding: "30px" }}>

            <h1>AI Fintech Dashboard</h1>

            {loanData && (
                <div>
                    <h2>Loan Eligibility</h2>
                    <p>
                        Eligible Loan:
                        ₹{loanData.eligible_loan}
                    </p>

                    <p>
                        Risk:
                        {loanData.risk}
                    </p>

                    <p>
                        Confidence:
                        {loanData.confidence}
                    </p>
                </div>
            )}

            {emiData && (
                <div>
                    <h2>Smart EMI</h2>

                    <p>
                        EMI:
                        ₹{emiData.emi}
                    </p>
                </div>
            )}

            {analytics && (
                <div>

                    <h2>Analytics</h2>

                    <p>
                        Risk Score:
                        {analytics.risk_score}
                    </p>

                    <p>
                        Stability:
                        {analytics.income_stability}
                    </p>

                    <p>
                        Volatility:
                        {analytics.volatility}
                    </p>

                    <h3>AI Alerts</h3>

                    <ul>
                        {analytics.alerts.map(
                            (alert, index) => (
                                <li key={index}>
                                    {alert}
                                </li>
                            )
                        )}
                    </ul>

                </div>
            )}

        </div>
    );
}

export default Dashboard;