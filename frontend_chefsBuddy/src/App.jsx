import './App.css'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import Inventory from './pages/Inventory'
import Navbar from "./components/Navbar"
import AddItem from "./pages/AddItem"
import NotFound from './pages/NotFound'
import SearchRecipe from './pages/SearchRecipe'
import RecipeDetails from './pages/RecipeDetails'
import SaveRecipe from './pages/SaveRecipe'

function App() {

  return (
    <Router>
      <div>
        <Navbar />

        <div>
          <Routes>

            <Route path = "/" element={<Inventory />} />
            <Route path = "/addItem" element={<AddItem />} />
            <Route path = "/recipe/search" element={<SearchRecipe />} />
            <Route path= "/recipe/details/:id" element={<RecipeDetails />} />
            <Route path= "/recipe/saveRecipe" element={<SaveRecipe />} />
            <Route path = "*" element={<NotFound />} />

          </Routes>
        </div>
      </div>
    </Router>
  )
}

export default App
