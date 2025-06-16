import { createTheme } from '@mui/material/styles';

// Colors
const apricot = '#FBCEB1';
const ginger = '#B65F34';
const darkBg = '#242424';
const white = '#ffffff';

const theme = createTheme({
  palette: {
    mode: 'dark',
    background: {
      default: darkBg,
      paper: darkBg,
    },
    text: {
      primary: white,
    },
    primary: {
      main: apricot,
    },
    secondary: {
      main: ginger,
    },
  },
  typography: {
    fontFamily: ['Roboto', 'Helvetica', 'Arial', 'sans-serif'].join(','),
    h1: { fontWeight: 700 },
    h2: { fontWeight: 600 },
    h3: { fontWeight: 600 },
    h4: { fontWeight: 500 },
    h5: { fontWeight: 500 },
    h6: { fontWeight: 500 },
    body1: { fontSize: '1rem' },
    body2: { fontSize: '0.875rem' },
  },
  components: {
    MuiPaper: {
      styleOverrides: {
        root: {
          backgroundColor: darkBg,
          color: white,
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          textTransform: 'none',
          fontWeight: 500,
        },
      },
      defaultProps: {
        variant: 'contained',
        color: 'primary',
      },
    },
    MuiChip: {
    defaultProps: {
      variant: 'outlined',
    },
    styleOverrides: {
      root: {
        borderRadius: 16, // same as Card (rounded)
        fontWeight: 500,
        backgroundColor: 'darkbg', // same as your Card background (or use darkBg variable)
        border: '0.75px solid apricot',
        color: '#ffffff',
      },
    },
  },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          boxShadow: '0 8px 24px rgba(0,0,0,0.3)',
        },
      },
    },
    MuiListItemButton: {
      styleOverrides: {
        root: {
          '&.Mui-selected': {
            backgroundColor: ginger,
          },
        },
      },
    },
  },
});

export default theme;
