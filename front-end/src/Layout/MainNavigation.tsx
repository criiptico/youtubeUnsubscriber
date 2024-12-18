import { Link } from "react-router-dom";

import classes from "./MainNavigation.module.css";

function MainNavigation(props){
    return (
        <header className={classes.header}>
            <Link><div className={classes.logo}>Filter YouTube Subscriptions</div></Link>
            <nav>
                <ul>
                    <li><Link to="/">Login</Link></li>
                    <li><Link to="/Profile">Profile</Link></li>
                    <li><Link to="/Filter">Filter</Link></li>
                </ul>
            </nav>
        </header>
    );
}

export default MainNavigation;