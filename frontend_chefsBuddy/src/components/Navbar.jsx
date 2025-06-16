import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import {Link, Typography} from '@mui/material';
import Button from '@mui/material/Button';
import {Link as RouterLink} from 'react-router-dom'
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

export default function Navbar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          {/* <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton> */}
            <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontWeight: 'bold' }}>
            <Link component={RouterLink} to="/" underline="none" color="inherit">
                chefsbuddy
            </Link>
            </Typography>
            
            <Button component={RouterLink} to="/" color="inherit">Home</Button>
            <Button component={RouterLink} to="/addItem" color="inherit">Add Item</Button>
            <Button component={RouterLink} to="#" color="inherit">Save Recipe</Button>
            <Button component={RouterLink} to="/recipe/search" color="inherit">Search Recipe</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}