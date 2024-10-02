import { createUseStyles } from 'react-jss';


const styles = createUseStyles ({
    // Main Container
    body: {
      fontFamily: 'andale mono',
      justifyContent: 'center',
      color: '#000000',
      backgroundColor: '#fff5d7',
      lineHeight: 1.5,
      display: 'flex',
      flexDirection: 'column',
      minHeight: '100vh',
      margin: 0,
      padding: 0
    },

    skillList: {
      listStyle: 'none',
    },

    // skills: {
    //   margin: '0 auto',
    //   // textAlign: 
    // },

    description1: {
      justifyContent: 'center',
      alignItems: 'center',
      alignContent: 'center',
      alignSelf: 'center'
    },

    socialItem: {
      display: 'inline-block',
      padding: '1px',
      alignSelf: 'center',
      margin: '1px 15px',
      borderRadius: '4px',
      '& a': {
        display: 'inline-block',
        textDecoration: 'none',
        color: '#ff5e6c',
      },
      '& a:hover': {
        color: '#000000',
        fontStyle: 'italic',
      },
    },

    // '*': {
    //   margin: '0',
    //   padding: '0',
    //   boxSizing: 'border-box',
    // },

    // animationWrapper: {
    //   display: 'flex',
    //   justifyContent: 'center',
    //   alignItems: 'center',
    // },
  
    // staticText: {
    //   fontSize: '60px',
    //   fontWeight: '400',
    // },
  
    // dynamicTexts: {
    //   listStyle: 'none',
    //   color: '#000000',
    //   fontSize: '60px',
    //   fontWeight: '500',
    //   position: 'relative',
    //   '&:after': {
    //     content: '""', // This should be a string
    //     position: 'absolute',
    //     left: '0',
    //     height: '100%',
    //     width: '100%',
    //     borderLeft: '2px solid #000000',
    //     animation: 'typing 3s steps(10) infinite', // Corrected animation property
    //   },
    // },
  
    // animationWrapperDynamicTexts: { // Split the combined selector
    //   marginLeft: '15px',
    //   lineHeight: '90px',
    //   height: '90px',
    // },
  
    // '@keyframes typing': {
    //   '40%': {
    //     left: '0',
    //   },
    //   '60%': {
    //     left: 'calc(100% + 30px)', // Remove semicolon
    //   },
    //   '100%': {
    //     left: '0',
    //   },
    // },

    socialMedia: {
      display: 'flex',
      justifyContent: 'center', // This will horizontally center the items
      alignItems: 'center', // This will vertically center the items if necessary
      alignContent: 'center'
    },
  
    // Main page title
    mainTitle: {
      margin: '10px 20px 0 20px',
      padding: 0
    },
  
    // Adding margins to sub-headings
    headings: {
      margin: '10px 10px 10px 20px'
    },
  
    // Adding line below each page heading
    header1: {
      '&:after': {
        content: '""',
        display: 'block',
        height: '2px',
        backgroundColor: '#FFFDD0',
        marginTop: '1px',
      },
    },
  
    // Main Navigation
    navItem: {
      display: 'inline-block',
      padding: '1px',
      margin: '1px 20px',
      '& a': {
        display: 'inline-block',
        textDecoration: 'none',
        color: '#000000',
      },
      '& a:hover': {
        color: '#ff5e6c',
        fontStyle: 'italic',
        borderRadius: '6px'
      },
    },
  
    // Active link
    activeNavItem: {
      '& a': {
        color: '#ff5e6c',
        display: 'inline-block',
      },
      '& a:hover': {
        color: '#ff5e6c',
        borderColor: '#ff5e6c',
      },
    },
  
    // Styling header/footer color
    header: {
      display: 'flex',
      flexDirection: 'column',
      background: '#fff5d7',
    },

    foot: {
      marginTop: 'auto',
      background: '#fff5d7',
      alignSelf: 'center',
      alignContent: 'center'
    },
  
    // Footer navigation
    footer: {
      marginTop: 'auto', // Keep footer at the bottom of the page
      '& nav': {
        '& li': {
          border: 'none',
        },
      },
    },
  
    // Style links in text
    link: {
      color: '#000000',
      textDecoration: 'none',
      '&:hover': {
        color: '#FFFDD0',
        textDecoration: 'wavy underline #FFFDD0',
      },
    },
  
    // Style elements in lists
    listItem: {
      color: '#000000',
    },
  
    // Copyright text
    copyright: {
      textAlign: 'center',
      color: '#000000',
    },
  
    // Styling text color in bullets and descriptions
    description: {
      color: '#000000',
      margin: '10px 20px 20px 20px',
      width: '75%',
    },
  
    // Style images and videos for Projects page
    media: {
      alignItems: 'center',
      display: 'flex',
      flexGrow: 1,
      maxWidth: '100%',
      height: 'auto',
      padding: '5px',
    },
  
    // Styling for Mobile devices
    '@media (max-width: 768px)': {
      navItem: {
        display: 'block',
        textAlign: 'left',
        margin: '10px 10px',
      },
      footerNavItem: {
        display: 'block',
        margin: 'auto auto',
      },
      socialMediaNavItem: {
        margin: 0,
      },
      footerNavItemBefore: {
        content: '"> "',
      },
    },
  });
  
export default styles;
  