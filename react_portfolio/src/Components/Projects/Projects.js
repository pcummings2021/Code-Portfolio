import React from 'react'
import Navigation from '../Navigation/Navigation'
import useStyles from '../Style/Style'
import forwardKinematics from './forward_kinematics.mp4'
import apptBooker from './appt_booker.png'


function Projects() {
    const classes = useStyles()

    return (
        <div className={classes.body}>
            <header className={classes.header}>
                <h1 class={classes.mainTitle}>Parker Cummings Resume</h1>
                <nav>
                    <Navigation/>
                </nav>
                <h2 class={classes.headings}>Projects</h2>
                <p class={classes.description}><em>This is a list of projects I have worked on and enjoyed during my academic career.</em></p>
            </header>

            <div class={classes.description}>
                <h3><em>Python GUI Appointment Booker</em></h3>
                <ul>
                    <li>This project is a GUI application created for scheduling appointments.</li>
                    <li>It uses the Python package PyQt5 to organize windows, control functionality, and more.</li>
                    <li>This project implements GUI design, as well as web scraping.</li>
                    <li>Holidays cannot be booked, the dates are pulled from Florida Tech's academic calendar
                        <ul>
                            <li>For the files, click here: <a class={classes.link} href="https://github.com/pcummings2021/Code-Portfolio/tree/main/appointment_booker">GitHub Link</a></li>
                        </ul>
                    </li>
                    <li>This image below shows the appearance of the GUI with an appointment booked
                        <img width="750" height = "400" src={apptBooker} alt="pic of appointment booker UI"/>
                    </li>
                </ul>
            </div>

            <div class={classes.description}>
                <h3><em>Forward Kinematics Robot Arm</em></h3>
                <ul>
                    <li>This project is a simple animation of a 3D-rendered robot arm using Forward Kinematics.
                        <ul>
                            <li>For a better description of forward kinematics, click here:
                                <a class={classes.link} href="https://www.sciencedirect.com/topics/engineering/forward-kinematics">Forward Kinematics</a></li>
                        </ul>
                    </li>
                    <li>The code implements the numpy package and matrix math to calculate each new angular plane.</li>
                    <li>Each plane where the angle on the arm changes is calculated using transformation matrices.</li>
                    <li>The 3D model itself is rendered using the Python Vedo Package.
                        <ul>
                            <li>For more on Vedo, click here: <a class={classes.link} href="https://vedo.embl.es/">Vedo documentation</a></li>
                        </ul>
                    </li>
                    <li>The video contains several screenshots with different parameters to show the arm's movement.</li>
                    <video width="750" height="400" src={forwardKinematics} controls>
                        <source src="forward_kinematics.mp4" type="video/mp4"/>
                    </video>
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
    )
}

export default Projects;