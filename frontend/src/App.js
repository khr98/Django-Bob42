//App.js
import React from "react";
import { BrowserRouter, Route, Routes} from "react-router-dom";
// src/pages/index.js를 통해서 한번에 import 할 수 있도록 함
import Main from './page/Main';
import Check from './page/Check';
import Login from './page/Login';
import Nav from './page/Nav';
import Reservation from './page/Reservation';
//import NotFound from "./NotFound";

const App = () => {
	return (
		<div className='App'>
			<BrowserRouter>
            <Nav/>
				<Routes>
					<Route path="/bob42" element={<Main />}></Route>
					<Route path="/bob42/login" element={<Login />}></Route>
                    <Route path="/bob42/reservation" element={<Reservation />}></Route>
                    <Route path="/bob42/reservation/check" element={<Check />}></Route>
					{/* 상단에 위치하는 라우트들의 규칙을 모두 확인, 일치하는 라우트가 없는경우 처리
					<Route path="*" element={<NotFound />}></Route> */}
				</Routes>
			</BrowserRouter>
		</div>
	);
};

export default App;
