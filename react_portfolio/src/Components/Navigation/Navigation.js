import { Link } from "react-router-dom";
import useStyles from "../Style/Style";

export default function Navigation() {
    const classes = useStyles();

    let links = [
        { href: "/", text: "About" },
        { href: "/skills", text: "Skills" },
        { href: "/projects", text: "Projects" },
        { href: "/resume", text: "Resume" },
        { href: "/contact", text: "Contact" }
    ];

    return (
        <nav>
            <ul>
                {links.map(link => (
                    <li className={classes.navItem} key={link.href}>
                        <Link to={link.href}>
                            {link.text}
                        </Link>
                    </li>
                ))}
            </ul>
        </nav>
    )
};
