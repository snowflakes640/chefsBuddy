import axios from "axios"
BASE_URL = "http://127.0.0.1:8000/api/"

const fetchInventoryData = async () => {
    try {
        const response = await axios.get(BASE_URL + 'inventory/');
        setData(response.data);
    } catch (error) {
        setError(error.message);
    }
};

export default fetchInventoryData