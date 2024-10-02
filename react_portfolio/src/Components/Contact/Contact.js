import React from 'react'
import Navigation from '../Navigation/Navigation'
import useStyles from '../Style/Style'

function Contact() {
    const classes = useStyles()

    return (
        <div className = {classes.body}>
            <header className = {classes.header}>
                <h1 class={classes.mainTitle}>Parker Cummings Resume</h1>
                <nav>
                    <Navigation/>
                </nav>
                <h2 className={classes.headings}>My Contact Information</h2>
            </header>

            <div class={classes.navItem}>
                <ul>
                    <li><strong>Personal Email:</strong> <a class={classes.link} href="mailto: pcummings884@gmail.com">pcummings884@gmail.com</a></li>
                    <li><strong>School Email:</strong>  <a class={classes.link} href="mailto: pcummings2021@my.fit.edu">pcummings2021@my.fit.edu</a></li>
                    <li><strong>Phone:</strong> <a class={classes.link} href="tel: 443-306-3443">443-306-3433</a></li>
                </ul>

                <h3>Input your information here:</h3>
                <ul>
                    <li>
                        <label for="flname">First and Last Name:</label>
                        <input type="text" id="flname" name="flname"/><br/><br/>
                    </li>
                    <li>
                        <label for="phone">Phone Number:</label>
                        <input type="text" id="phone" name="phone"/><br/><br/>
                    </li>
                    <li>
                        <label for="email">Email:</label>
                        <input type="text" id="email" name="email"/><br/><br/>
                    </li>
                </ul>
            </div>

            <footer class={classes.foot}>
                <nav class={classes.footer}>
                    <Navigation/>
                </nav>
                <nav class={classes.socialMedia}>
                    <ul>
                        <li className={classes.socialItem}><a href="https://www.instagram.com/_parkercummings/">Instagram</a></li>
                        <li className={classes.socialItem}><a href="https://www.linkedin.com/in/parker-cummings1/">LinkedIn</a></li>
                        <li className={classes.socialItem}><a href="https://www.facebook.com/profile.php?viewas=100000686899395&id=100070692668865">Facebook</a></li>
                    </ul>
                </nav>
                <div class={classes.copyright}>
                    <p>© Parker Cummings 2024</p>
                </div>
            </footer>
        </div>
    );
}


export default Contact;