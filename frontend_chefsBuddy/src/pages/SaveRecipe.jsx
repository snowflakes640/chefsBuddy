import { useState } from "react"
import axios from "axios"
import { TextField, Button, Typography, Paper, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio, Container, Stack } from "@mui/material";
import FormGroup from "@mui/material/FormGroup";
import Checkbox from "@mui/material/Checkbox";;




const SaveRecipe = () => {
    const BASE_URL = "http://127.0.0.1:8000/api/"
    // const [message, setMessage] = useState("")
    const [formData, setFormData] = useState({
        id: "",
        title: "",
        rating: "",
        category: "",
        prep_time: "",
        servings: "",
        ingredients: "",
        instructions: "",
        recipe_url: ""

    })

    function handleInfoChange(e) {
        const {name, value} = e.target
        setFormData((prev) => ({...prev,
            [name]: value
        }))
    }

    const handleSubmit = async(event) => {
        event.preventDefault()
        try{
            await axios.post(BASE_URL + "recipe/saveRecipe/", submissionData)
            alert("Your recipe is saved!!!")
            setFormData({
                name: "",
                quantity: "",
                unit: "",
                expiry_date: null
            })
        } catch(error) {
            alert("Error:" + error.message)

        }
    }
    return (
        // <form onSubmit={handleSubmit}>

        // <legend><h1>Add item to inventory</h1></legend>

        // <label htmlFor="ingredName"> Name of ingredient: </label>
        // <input 
        // type="text" 
        // name="name" 
        // id="ingredName"
        // value = {formData.name}
        // onChange={handleInfoChange}
        // /> <br />
        
        // <label htmlFor="ingredAmount"> Amount of ingredient: </label>
        // <input 
        // type="text" 
        // name="quantity" 
        // id="ingredAmount"
        // value = {formData.quantity}
        // onChange={handleInfoChange}
        // /> <br />

        // <label > Unit of ingredient: </label> <br/>
        // <input
        // type="radio"
        // id="Litre"
        // name="unit"
        // value="Litre"
        // checked={formData.unit === "Litre"}
        // onChange={handleInfoChange}/>

        // <label htmlFor="Litre"> Litre </label> <br/>
        // <input 
        // type="radio"
        // id="Kilogram"
        // name="unit"
        // value="Kilogram"
        // checked={formData.unit === "Kilogram"}
        // onChange={handleInfoChange}/>
        
        // <label htmlFor="Kilogram"> Kilogram </label> <br/>
        // <input 
        // type="radio"
        // id="Unit"
        // name="unit"
        // value="Unit"
        // checked={formData.unit === "Unit"}
        // onChange={handleInfoChange}/>
        
        // <label htmlFor="Unit"> Unit </label> <br/>
        
        // <label htmlFor="expireDate"> Choose estimated expiry date: </label>
        // <input 
        // type="date"
        // id="expireDate"
        // name="expiry_date"
        // value={formData.expiry_date}
        // defaultValue = "Not applied"
        // onChange={handleInfoChange}/> <br /> <br />
        // </form>

    
      <Container maxWidth="md" sx={{ mt: 5 }}>
      <Paper elevation={2} sx={{ padding: 4 }}>
        <Typography gutterBottom variant="h4" align="center">
          Add item to your inventory!
        </Typography>

        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField
              fullWidth
              id="ingredName"
              label="Ingredient Name"
              name="name"
              variant="outlined"
              value={formData.name}
              onChange={handleInfoChange}
              required
            />

            <TextField
              fullWidth
              id="ingredAmount"
              label="Ingredient Amount"
              type="number"
              name="quantity"
              variant="outlined"
              value={formData.quantity}
              onChange={handleInfoChange}
              inputProps={{ min: 0}}
              required
            />

            <FormControl>
              <FormLabel>Choose Ingredient Unit</FormLabel>
              <RadioGroup
                name="unit"
                value={formData.unit}
                onChange={handleInfoChange}
              >
                <FormControlLabel value="Unit" control={<Radio />} label="Unit" />
                <FormControlLabel value="Kilogram" control={<Radio />} label="Kilogram" />
                <FormControlLabel value="Litre" control={<Radio />} label="Litre" />
                <FormControlLabel value="Other" control={<Radio />} label="Other" />
              </RadioGroup>
            </FormControl>

            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DatePicker
                id="expireDate"
                label="Estimated Expiry Date"
                value={formData.expiry_date}
                onChange={handleDateChange}
                slotProps={{
                  textField: { fullWidth: true, variant: "outlined", name: "expiry_date" }
                }}
              />
            </LocalizationProvider>

            <Button fullWidth type="submit" variant="contained" size="large">
              Save
            </Button>
          </Stack>
        </form>
      </Paper>
    </Container>

    
    )
}

export default SaveRecipe