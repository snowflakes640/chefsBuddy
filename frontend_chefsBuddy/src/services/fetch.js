import axios from "axios"

const BASE_URL = "http://127.0.0.1:8000/api/"

export const fetchRecipe = async (searchTerm) => {
  const getResponse = await axios.get(BASE_URL + "recipe/showList/", {
    params: {
      q: searchTerm,
    },
  });

  const response = await getResponse.data;

  const parseCategory = (category) => {
    if (Array.isArray(category)) {
      return category;
    } else if (typeof category === "string") {
      return category.split(",").map(item => item.trim()).filter(Boolean);
    } else {
      return [];
    }
  };

  const parsedResponse = response.map(recipe => ({
    ...recipe,
    category: parseCategory(recipe.category),
  }));

  return parsedResponse;
};


// export const fetchRecipe = async(searchTerm) => {
//         const getResponse = await axios.get(BASE_URL + "recipe/showList/", {
//             params:{
//                 q: searchTerm
//             }
//         })
//         // console.log(getResponse)

//         const response = await getResponse.data

//         return response

//         // const data = await response.json()
//         // return data.results
// }

export const fetchDetails = async(recipeID) => {
        const getResponse = await axios.get(`${BASE_URL}recipe/details/${recipeID}/`)
        // console.log(getResponse)

        const response = getResponse.data
        return response
}

        