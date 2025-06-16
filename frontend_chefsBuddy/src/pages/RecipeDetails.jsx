import React, { useEffect, useState } from 'react';
import { useParams } from "react-router-dom";
import { fetchDetails } from "../services/fetch";
import { Rating, Chip, List, ListItem, ListItemText, Typography, Stack, Paper, Card, CardContent } from '@mui/material';

const RecipeDetails = () => {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  // Universal parser for ingredients
  const parseIngredients = (ingredients) => {
    if (Array.isArray(ingredients)) {
      return ingredients;
    } else if (typeof ingredients === "string") {
      return ingredients.split(",").map(item => item.trim()).filter(Boolean);
    } else {
      return [];
    }
  };

  // Universal parser for category
  const parseCategory = (category) => {
    if (Array.isArray(category)) {
      return category;
    } else if (typeof category === "string") {
      return category.split(",").map(item => item.trim()).filter(Boolean);
    } else {
      return [];
    }
  };

  useEffect(() => {
    const getRecipeDetails = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await fetchDetails(id);
        setRecipe(response[0]);
        console.log(response)
      } catch (err) {
        setError(err.message || "Failed to fetch recipe details.");
        setRecipe(null);
      } finally {
        setLoading(false);
      }
    };
    getRecipeDetails();
  }, [id]);

  if (loading) return <Typography variant="h5" align="center" mt={4}>Loading...</Typography>;
  if (error) return <Typography variant="h5" color="error" align="center" mt={4}>Error: {error}</Typography>;
  if (!recipe) return <Typography variant="h5" align="center" mt={4}>No recipe found</Typography>;

  const ingredientsArray = parseIngredients(recipe.ingredients);
  const categoryArray = parseCategory(recipe.category);
  const instructionsArray = Array.isArray(recipe.instructions) ? recipe.instructions : [];

  return (
    <Paper elevation={3} sx={{ width: '60%', mx: 'auto', my: 4, p: 4 }}>
      <Typography variant="h4" gutterBottom>{recipe.title ?? "Untitled Recipe"}</Typography>

      <Stack direction="row" alignItems="center" spacing={1} mb={2}>
        <Rating value={typeof recipe.rating === "number" ? recipe.rating : 0} precision={0.1} readOnly />
        <Typography variant="body2">({recipe.rating ?? "N/A"})</Typography>
      </Stack>

      <Typography variant="body1" mb={1}>Prep Time: {recipe.prep_time ?? "N/A"}</Typography>
      <Typography variant="body1" mb={1}>Servings: {recipe.servings ?? "N/A"}</Typography>

      <Typography variant="h6" gutterBottom>Categories:</Typography>
      <Stack direction="row" spacing={1} flexWrap="wrap" mb={2}>
        {categoryArray.length > 0 ? (
          categoryArray.map((cat, index) => (
            <Chip key={index} label={cat} />
          ))
        ) : (
          <Typography variant="body2">No categories</Typography>
        )}
      </Stack>

      <Typography variant="h6" gutterBottom>Ingredients:</Typography>
      <List dense>
        {ingredientsArray.map((item, index) => (
          <ListItem key={index}>
            <ListItemText primary={item} />
          </ListItem>
        ))}
      </List>

      <Typography variant="h6" gutterBottom>Instructions:</Typography>
      <List dense>
        {instructionsArray.map((step, index) => (
          <ListItem key={index}>
            <ListItemText primary={`${index + 1}. ${step}`} />
          </ListItem>
        ))}
      </List>
    </Paper>



    // <Card key={recipe.id} sx={{ maxWidth: 600, m: '20px auto', boxShadow: 3, borderRadius: 3 }}>
    //   <CardContent>
    //     <Typography variant="h4" component="div" gutterBottom>{recipe.title || "Untitled Recipe"}</Typography>

    //     <Stack direction="row" alignItems="center" spacing={1} mb={1}>
    //       <Rating value={typeof recipe.rating === "number" ? recipe.rating : 0} precision={0.1} readOnly />
    //       <Typography variant="body2">({recipe.rating ?? "N/A"})</Typography>
    //     </Stack>

    //     <Typography variant="body2" color="text.secondary" mb={2}>
    //       Prep Time: {recipe.prep_time || "N/A"} | Servings: {recipe.servings || "N/A"}
    //     </Typography>

    //     <Stack direction="row" spacing={1} flexWrap="wrap" mb={2}>
    //       {categoryArray.length > 0 ? (
    //         categoryArray.map((cat, index) => (
    //           <Chip key={index} label={cat} color="primary" variant="outlined" />
    //         ))
    //       ) : (
    //         <Typography variant="body2" color="text.secondary">No categories</Typography>
    //       )}
    //     </Stack>

    //     <Typography variant="h6" gutterBottom>Ingredients:</Typography>
    //     {ingredientsArray.length > 0 ? (
    //       <List dense>
    //         {ingredientsArray.map((item, index) => (
    //           <ListItem key={index}>
    //             <ListItemText primary={item} />
    //           </ListItem>
    //         ))}
    //       </List>
    //     ) : (
    //       <Typography variant="body2" color="text.secondary" mb={2}>No ingredients listed.</Typography>
    //     )}

    //     <Typography variant="h6" gutterBottom>Instructions:</Typography>
    //     {instructionsArray.length > 0 ? (
    //       <List dense>
    //         {instructionsArray.map((step, index) => (
    //           <ListItem key={index}>
    //             <ListItemText primary={`${index + 1}. ${step}`} />
    //           </ListItem>
    //         ))}
    //       </List>
    //     ) : (
    //       <Typography variant="body2" color="text.secondary">No instructions available.</Typography>
    //     )}
    //   </CardContent>
    // </Card>
  );
};

export default RecipeDetails;
