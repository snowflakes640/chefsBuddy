import { useState, useEffect } from "react"
import axios from "axios"
import { Box, Typography, List, ListItem, ListItemText } from "@mui/material"

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
        <Box sx={{ ml: 10, mt: 8 }}>

            <Typography variant="h3"> Currently in inventory: </Typography>
            <List sx={{ width: '100%', bgcolor: 'background.paper' }}>
                {data.map((item) => (
                    <ListItem key={item.id}>
                    <ListItemText
                        primary={
                            <Typography variant="h5" fontWeight="bold">
                                {item.name} — {item.quantity} {item.unit}
                            </Typography>}
                        secondary={
                            <Typography variant="subtitle">
                            Expires on: {item.expiry_date || 'N/A'}<br />
                            Last stocked on: {item.last_stocked || 'N/A'}
                        </Typography>
                        }
                        />
                    </ListItem>
                ))}
            </List>
        </Box>
            {/* <ul>
                {
                    data.map((item) => (
                                <li key={item.id}> <strong>{item.name}: </strong> {item.quantity} {item.unit} expires on - {item.expiry_date} <br></br> 
                                Last stocked on - {item.last_stocked} <br></br>
                                <br></br></li>
                    ))
                }
            </ul> */}
    
    </>
    )
}

export default Inventory