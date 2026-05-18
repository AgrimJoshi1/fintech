const BASE_URL = "http://127.0.0.1:8000";

export async function adjustEMI(data) {

    const response = await fetch(
        `${BASE_URL}/adjust-emi`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    return response.json();
}