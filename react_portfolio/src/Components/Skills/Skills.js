import React from 'react'
import Navigation from '../Navigation/Navigation'
import useStyles from '../Style/Style'


function Skills() {
    const classes = useStyles();

    return (
        <div className={classes.body}>
            <header className={classes.header}>
                <h1 class={classes.mainTitle}>Parker Cummings Resume</h1>
                <nav>
                    <Navigation/>
                </nav>
                <h2 class={classes.headings}>Marketable Skills</h2>
            </header>

            <div className={classes.skills}>
                <ul class={classes.skillList}>
                    <li>Object-Oriented Programming</li>
                    <li>Python</li>
                    <li>Java</li>
                    <li>Cloud Security/Data Security</li>
                    <li>Web Application Development</li>
                    <li>C/C++</li>
                    <li>Algorithms and Data Structures</li>
                    <li>Terraform/Cloud IaaC</li>
                    <li>AWS Certified Cloud Practitioner</li>
                    <li>Basic Assembly Language</li>
                    <li>Software Development/Testing</li>
                    <li>Requirements Analysis/Engineering</li>
                    <li>Customer-facing meetings</li>
                    
                </ul>
            </div>

            <footer className={classes.foot}>
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

export default Skills;