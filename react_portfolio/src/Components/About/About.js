import React from 'react'
import Navigation from '../Navigation/Navigation'
import useStyles from '../Style/Style'

function About() {
    const classes = useStyles()

    return (
        <div className={classes.body}>
            <header className={classes.header}>
                <h1 className={classes.mainTitle}>Parker Cummings Resume</h1>
                <nav>
                    <Navigation />
                </nav>
                <h2 className={classes.headings}>About Me</h2>
            </header>
            <div className={classes.description1}>
                <p className={classes.description}>
                    Hello! My name is Parker Cummings, and I am a current Junior at Florida Tech
                    studying Computer Science. My areas of highest experience include object-oriented programming,
                    basic Cyber Operations, and logical problem-solving. I am originally from Severna Park, MD,
                    and I am expecting to graduate in May 2025. I am actively seeking any internship opportunities
                    in software engineering, software development, or computer science.
                </p>
            </div>
            {/* <div className={classes.animationWrapper}>
                <div className={classes.staticText}>I'm</div>
                <ul className={classes.dynamicTexts}>
                    <li><span>Learner</span></li>
                    <li><span>Educator</span></li>
                    <li><span>Leader</span></li>
                    <li><span>Student</span></li>
                    <li><span>Hardworker</span></li>
                    <li><span>Problem Solver</span></li>
                    <li><span>Valuble Team Member</span></li>
                </ul>
            </div> */}
            <footer className={classes.foot}>
                <nav className={classes.footer}>
                    <Navigation />
                </nav>
                <nav className={classes.socialMedia}>
                    <ul>
                        <li className={classes.socialItem}><a href="https://www.instagram.com/_parkercummings/">Instagram</a></li>
                        <li className={classes.socialItem}><a href="https://www.linkedin.com/in/parker-cummings1/">LinkedIn</a></li>
                        <li className={classes.socialItem}><a href="https://www.facebook.com/profile.php?viewas=100000686899395&id=100070692668865">Facebook</a></li>
                        <li className={classes.socialItem}><a href="https://github.com/pcummings2021/Code-Portfolio">Github</a></li>
                    </ul>
                </nav>
                <div className={classes.copyright}>
                    <p>© Parker Cummings 2024</p>
                </div>
            </footer>
        </div>
    );
}

export default About;
