import React, { useState } from 'react';
import { Box, Button, Rating, Chip, List, ListItem, ListItemText, ListItemButton, Typography, Stack, CardHeader, TextField, IconButton, Card, CardContent, Paper, Divider, Alert } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import {fetchRecipe, fetchDetails} from "../services/fetch"
import { useNavigate } from 'react-router-dom';

function SearchRecipe(){
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(null)
  const [error, setError] = useState(null)
  const [searchTerm, setSearchTerm] = useState('');
  const navigate = useNavigate()
  
  const handleSearch = (event) => {
      setSearchTerm(event.target.value);
  };

  const handleSubmit = async(event) => {
    event.preventDefault()
    setLoading(true)
    try{
        const response = await fetchRecipe(searchTerm)
        console.log(response)
        setData(response)
        setLoading(false)
    } catch(error) {
        console.log(error)
        setError(error.message)
        setLoading(false)
    }
  }

  if (error) return <div> Error: {error} </div>

  const handleRecipeClick = (recipeID) => {
     navigate(`/recipe/details/${recipeID}`)
  }
  //   try{
  //       const response = await fetchDetails(recipeID)
  //       console.log(response)
        
       
  //   } catch(error) {
  //       console.log(error)
  //       return <Alert> {error.message} </Alert>
  //   }
  // }

  return (
    <>
    <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '20vh' }}>
      <Paper component="form" onSubmit={handleSubmit} sx={{ p: 2, display: 'flex', width: '50%' }}>
        <TextField
          label="Search Recipe"
          variant="outlined"
          placeholder="Search Recipe"
          value={searchTerm}
          onChange={handleSearch}
          fullWidth
          sx={{ input: { color: 'white' } }}
        />
        <IconButton type="submit" sx={{ p: 1 }}>
          <SearchIcon sx={{ color: 'primary.main' }} />
        </IconButton>
      </Paper>
    </Box>

    {!loading ? (
      data.length === 0 ? (
        <Typography align="center" variant="h5" mt={4}>No recipe found</Typography>
      ) : (
        <Box sx={{ display: 'flex', justifyContent: 'center', flexWrap: 'wrap', gap: 3, p: 2 }}>
          {data.map((recipe) => (
            <Card key={recipe.id} sx={{ width: 300 }}>
              <CardContent>
                <Typography variant="h6" gutterBottom>{recipe.title}</Typography>
                <Stack direction="row" alignItems="center" spacing={1} mb={1}>
                  <Rating value={recipe.rating ?? 0} precision={0.1} readOnly />
                  <Typography variant="body2">({recipe.rating ?? "N/A"})</Typography>
                </Stack>
                <Typography variant="body2" gutterBottom>Prep Time: {recipe.prep_time ?? "N/A"}</Typography>
                <Typography variant="body2" gutterBottom>Servings: {recipe.servings ?? "N/A"}</Typography>
                <Typography variant="body2" gutterBottom>Source: {recipe.source ?? "N/A"}</Typography>
                {/* <Typography variant="body2" gutterBottom>Category: {recipe.category ?? "N/A"}</Typography> */}
                <Typography variant="body2" gutterBottom>Categories:</Typography>
                      <Stack direction="row" spacing={1} flexWrap="wrap" mb={2}>
                        {recipe.category.length > 0 ? (
                          recipe.category.map((cat, index) => (
                            <Chip key={index} label={cat} />
                          ))
                        ) : (
                          <Typography variant="body2">No categories</Typography>
                        )}
                      </Stack>
                <Box sx={{ p: 2 }}>
                <Button fullWidth onClick={() => handleRecipeClick(recipe.id)}>View Details</Button>
              </Box>
              </CardContent>
            </Card>
          ))}
        </Box>
      )
    ) : (
      <Typography align="center" variant="h5" mt={4}>Loading...</Typography>
    )}
  </>

    
    // <>
    //   <Paper
    //     component="form"
    //     onSubmit={handleSubmit}
    //     sx={{ p: '25px 4px', display: 'flex', alignContent: 'center', width: .5 }}
    //   >
    //     <TextField
    //       label= "Search Recipe"
    //       variant= "outlined"
    //       placeholder="Search Recipe"
    //       value={searchTerm}
    //       onChange={handleSearch}
    //     />
    //     <IconButton
    //       type="submit"
    //       sx={{ p: '10px'}}
    //       aria-label="search">
    //       <SearchIcon />
    //     </IconButton>
    //     <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
    //   </Paper>

    //   {!loading ? (
    //     data.length === 0 ? (
    //       <h1>no recipe</h1>
    //     ) : (
    //       <div>
    //         {data.map((recipe) => (
    //           <Box key={recipe.id} sx={{ width:.5, backgroundColor:"#465A7E66", my: 1 }}>
    //           <nav aria-label="Search Result Recipe">
    //             <List>
    //               <ListItem disablePadding>
    //                 <ListItemButton onClick={() => handleRecipeClick(recipe.id)}>
    //                   <ListItemText primary={recipe.title} />
    //                 </ListItemButton>
    //               </ListItem>
    //             </List>
    //           </nav>
    //           </Box>
    //         ))}
    //       </div>
    //     )
    //   ) : (
    //     <h1>loading ...</h1>
    //   )}
    // </>
  )
}

export default SearchRecipe
