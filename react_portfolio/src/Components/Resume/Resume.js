import React from 'react'
import Navigation from '../Navigation/Navigation'
import useStyles from '../Style/Style'


function Resume() {
    const classes = useStyles();

    return (
        <div className={classes.body}>
            <header className={classes.header}>
                <h1 class={classes.mainTitle}>Parker Cummings Resume</h1>
                <nav>
                    <Navigation/>
                </nav>
                <h2 class={classes.headings}>Resume</h2>
                <p class={classes.description}><em>Here, you can find relevant work/volunteer experience as well as my education.</em></p>
            </header>

            <div class={classes.description}>
                <h3><em>Education</em></h3>
                <ul>
                    <li><strong>Florida Institute of Technology - </strong><em>Melbourne, FL</em>
                        <ul>
                            <li>Major: Computer Science</li>
                            <li>Current year: Junior</li>
                            <li><strong>Current GPA: 3.82</strong></li>
                            <li>Expected Grad: May 2025</li>
                            <li>Relevant Coursework: Algorithms, Data Structures, Operating Systems, Computer Architecture/Assembly, <br/>
                                Java Programming, Python Programming, Intro to Cyber Operations</li>
                            <li>Activities and Societies: Order of Omega, Pi Kappa Alpha, Phi Eta Sigma, Rock Climbing Club, SGA</li>
                        </ul>
                    </li>
                    <li><strong>Severna Park High School - </strong><em>Severna Park, MD</em>
                        <ul>
                            <li>High School Diploma</li>
                            <li>Graduated: June 2021</li>
                            <li>GPA: 3.78</li>
                            <li>Relevant Coursework: Physics, Calculus, Statistics, Writing, <a class="classes.link" href="https://www.pltw.org/">PLTW* (Project Lead the Way)</a></li>
                            <li>Activities and Societies: National Honor Society, PLTW</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class={classes.description}>
                <h3><em>Experience</em></h3>
                <ul>
                    <li><strong>Software Engineering Intern - Avidyne Corporation, </strong><em>Melbourne, FL (May 2023 - Pres.)</em>
                        <ul>
                            <li><em>Employed for a full-time internship for the Summer of 2023, currently working part-time in continuation<br/>
                                with my completion of courses in the Fall 2023 and Spring 2024 semester. Responsibilities include:</em>
                            <ul>
                                <li>Collaborated with systems engineers, support engineers, and end customers to define, develop, and <br/>
                                    integrate Avidyne’s next-generation products.</li>
                                <li>Assisted the dynamic software development team in implementing a wide range of software features, ranging <br/>
                                    from low-level operating system layers to high-resolution, touchscreen-based HMI layers.</li>
                                <li>Conducted software verification activities to ensure quality and reliability.</li>
                                <li>Contributed to evaluating FAA-mandated requirements for aviation products.</li>
                                <li>Worked on expanding Avidyne’s simulation and test capabilities.</li>
                                <li>Developed and improved tools for tracking and automating software development activities.</li>
                            </ul>
                            </li>
                        </ul>
                    </li>
                    <li><strong>Chapter President - Pi Kappa Alpha Fraternity, </strong><em>Melbourne, FL (Mar 2023 - Dec 2023)</em>
                    <ul>
                        <li><em>Chosen by the Executive Council and Chapter members to take the position as only a sophomore <br/>
                            after the acting President could no longer serve his term. Responsibilities include:</em>
                            <ul>
                                <li>Oversight of 65+ chapter members through social, financial, and logistical hardships</li>
                                <li>Lead and oversaw weekly meetings with the entire chapter, as well as two meetings per week with <br/>the members of the Executive Council</li>
                                <li>Combined with the efforts of the Treasurer to oversee roughly $100,000 in expenses per year</li>
                                <li>Represented chapter with the Council of Presidents (COP) consisting of monthly meetings with <br/>the Director of Greek life and presidents of other on-campus greek organizations</li>
                                <li>Maintained positive relationship/consistent communication with chapter alumni, Director of Greek life,<br/>partnering philanthropy/community service organizations, etc.</li>
                            </ul>
                            </li>
                    </ul>
                    </li>
                    <li><strong>Dock-master, Crew member - Magothy Marina, </strong><em>Severna Park, MD (Feb 2018 - Aug 2022)</em>
                        <ul>
                            <li><em>Part-time employee during school year (fall, winter, and spring) and full-time employee throughout Summer.<br/>Promoted to Dock-master effective August 2020.</em>
                                <ul>
                                    <li>Gained valuable customer experience and problem-solving skills through interaction with marina slip owners.</li>
                                    <li>Filed contracts, financial reconciliation, fuel transactions and other marine services support.</li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class={classes.description}>
                <p class={classes.description}><em>If you have any other questions about my education/experience, please reference the contact page.</em></p>
                <h4>*PLTW is a 4-year engineering program set to introduce students to principles of being an engineer. <br/>
                    Topics covered include Thermodynamics, Computer Aided Design, Engineering Design, and Digital Electronics.</h4>
            </div>

            <footer>
                <nav>
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

export default Resume;