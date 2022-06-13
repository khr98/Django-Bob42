import React from "react";
import { Link } from "react-router-dom";

function Nav() {
  return (
    <>
      <Link to="/bob42">
        <button>메인 화면으로</button>
      </Link>
      <Link to="/bob42/login">
        <button>로그인 화면으로</button>
      </Link>
      <Link to="/bob42/reservation">
        <button>reservation 화면으로</button>
      </Link>
	  <Link to="/bob42/reservation/check">
        <button>reservation_check 화면으로</button>
      </Link>
    </>
  );
}

export default Nav;