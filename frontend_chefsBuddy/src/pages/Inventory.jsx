import { useState, useEffect } from "react"
import axios from "axios"

const Inventory = () => { 
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null)
    const BASE_URL = "http://127.0.0.1:8000/api/"

    useEffect(() => {
        const fetchData = async() => {
        try{
            const response = await axios.get(BASE_URL + "inventory/")
            setData(response.data)
            setLoading(false)
        } catch(error) {
            setError(error.message)
            setLoading(false)
        }}

        fetchData()
    }, [])

    if (loading) return <div> Loading... </div>
    if (error) return <div> Error: {error} </div>
    
    return(
        <>
            <h1> Currently in inventory: </h1>
            <ul>
                {
                    data.map((item) => (
                                <li key={item.id}> <strong>{item.name}: </strong> {item.quantity} {item.unit} expires on - {item.expiry_date} <br></br> 
                                Last stocked on - {item.last_stocked} <br></br>
                                <br></br></li>
                    ))
                }
            </ul>
    
    </>
    )
}

export default Inventory