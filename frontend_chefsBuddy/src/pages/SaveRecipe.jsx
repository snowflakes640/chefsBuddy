import { useState } from "react"
import axios from "axios"
import { Divider, MenuItem, TextField, Button, Typography, Paper, FormControl, FormLabel, RadioGroup, FormControlLabel, Radio, Container, Stack } from "@mui/material";
import FormGroup from "@mui/material/FormGroup";
import Checkbox from "@mui/material/Checkbox";;




const SaveRecipe = () => {
  const BASE_URL = "http://127.0.0.1:8000/api/"
    // const [message, setMessage] = useState("")
  const [formData, setFormData] = useState({
    title: "",
    rating: "",
    category: "",
    prep_time: "",
    servings: "",
    ingredients: "",
    instructions: "",
    recipe_url: ""
    })



  const categoryList = [
    {
      value: 'Meat and Poultry',
      label: 'Meat & Poultry',
    },
    {
      value: 'BBQ and Grilling',
      label: 'BBQ & Grill',
    },
    {
      value: 'Seafood',
      label: 'Seafood',
    },
    {
      value: 'Soups & stew',
      label: 'Soups & stew',
    },
    {
      value: 'Salad',
      label: 'Salad',
    },
    {
      value: 'Fruits and Vegetables',
      label: 'Fruits & Veg',
    },
    {
      value: 'Bread',
      label: 'Bread',
    },
    {
      value: 'Drinks',
      label: 'Drinks',
    },
    {
      value: 'Desserts',
      label: 'Desserts',
    },
    {
      value: 'Main Dish',
      label: 'Main Dish',
    },
    {
      value: 'Side Dish',
      label: 'Side Dish',
    },
    {
      value: 'Appetizers and Snacks',
      label: 'Appetizers & Snacks',
    },
    {
      value: 'Breakfast and Brunch',
      label: 'Breakfast & Brunch',
    },
    {
      value: 'Everyday Cooking',
      label: 'Everyday Cooking',
    },
  ]

  function handleInfoChange(e) {
      const {name, value} = e.target
      setFormData((prev) => ({...prev,
          [name]: value
      }))
  }

  const handleSubmit = async (event) => {
  event.preventDefault();

  try {
    const validData = {
      ...formData,
      rating: formData.rating === "" ? null : parseFloat(formData.rating),
      servings: formData.servings === "" ? null : parseInt(formData.servings),
      instructions: formData.instructions
        .split("\n")
        .filter(Boolean), // convert multiline string to array
    };

    await axios.post(BASE_URL + "recipe/saveRecipe/", validData);
    alert("Your recipe is saved!!!");

    // Reset form
    setFormData({
      title: "",
      rating: "",
      category: "",
      prep_time: "",
      servings: "",
      ingredients: "",
      instructions: "",
      recipe_url: "",
    });
  } catch (error) {
    alert("Error: " + error.message);
    console.error(error.response?.data || error);
  }
};
    return (
    
      <Container maxWidth="md" sx={{ mt: 5 }}>
      <Paper elevation={2} sx={{ padding: 4 }}>
        <Typography gutterBottom variant="h4" align="center">
          Save your recipe!
        </Typography>

        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <TextField
              fullWidth
              id="title"
              label="Name of the recipe"
              name="title"
              variant="outlined"
              value={formData.title}
              onChange={handleInfoChange}
              required
            />

            <Divider>About the recipe</Divider>

            <TextField
              fullWidth
              id="rating"
              label="Rate the recipe"
              type="number"
              name="rating"
              variant="outlined"
              value={formData.rating}
              onChange={handleInfoChange}
              inputProps={{ min: 0, max: 5, step: 0.1 }}
            />

            <TextField
              fullWidth
              id="prep_time"
              label="Estimated preparation time"
              type="text"
              name="prep_time"
              variant="outlined"
              value={formData.prep_time}
              onChange={handleInfoChange}
            />

            <TextField
              fullWidth
              id="servings"
              label="Serving for"
              type="number"
              name="servings"
              variant="outlined"
              value={formData.servings}
              onChange={handleInfoChange}
            />

            <TextField
              fullWidth
              id="recipe_url"
              label="Original source link"
              type="text"
              name="recipe_url"
              variant="outlined"
              value={formData.recipe_url}
              onChange={handleInfoChange}
            />

            <TextField
            id="category"
            select
            name="category"
            label="Choose a category"
            defaultValue="Main Dish"
            >
            {categoryList.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
            </TextField>

            <Divider>Details of the recipe</Divider>

            <TextField
              fullWidth
              id="ingredients"
              label="ingredients"
              type="text"
              name="ingredients"
              variant="outlined"
              value={formData.ingredients}
              onChange={handleInfoChange}
              multiline
              maxRows={4}
              required
            />

            <TextField
              fullWidth
              id="instructions"
              label="instructions"
              type="text"
              name="instructions"
              variant="outlined"
              value={formData.instructions}
              onChange={handleInfoChange}
              multiline
              maxRows={35}
              required
            />


            <Button fullWidth type="submit" variant="contained" size="medium">
              Save
            </Button>
          </Stack>
        </form>
      </Paper>
    </Container>    
    )
}

export default SaveRecipe