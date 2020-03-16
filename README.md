# Ekşisözlük Unofficial API Documentation - 2020
$ denotes a variable.
### API Details
<table>
	<tbody>
		<tr>
			<td>Host</td>
			<td>api.eksisozluk.com</td>
		</tr>
		<tr>
			<td>Protocol</td>
			<td>SSL</td>
		</tr>
	</tbody>
</table>

### Required Headers
<table>
	<thead>
		<tr>
			<th>Header</th>
			<th>Example</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>authorization</td>
			<td>bearer $token</td>
		</tr>
		<tr>
			<td>Content-type</td>
			<td>application/json</td>
		</tr>
		<tr>
			<td>User-agent</td>
			<td>okhttp/2.3.0</td>
		</tr>
	</tbody>
</table>

### Known Endpoints

<table>
   <thead>
      <tr>
         <th>Endpoint</th>
         <th>Purpose</th>
         <th>Data</th>
         <th>Method</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>/token</td>
         <td>Returns bearer token. This end point uses content-type: application/x-www-form-urlencoded.</td>
         <td>{'grant_type': 'password', 'username': 'INSERT_USERNAME', 'password': 'INSERT_PW', 'client_secret': 'INSERT_CS_HERE'}</td>
         <td>POST</td>
      </tr>
	  <tr>
		 <td>/v1/topic/$topic-id</td>
		 <td>Returns a page of topic.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/entry/$entry-id</td>
		 <td>Returns an entry.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/popular</td>
		 <td>Returns a page of popular/gündem topics.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/feed/entry</td>
		 <td>Returns entries of people you follow.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/feed/favorites</td>
		 <td>Returns favorites of people you follow.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/caylak</td>
		 <td>Returns çaylak topics.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/todayinpast/$year</td>
		 <td>Returns todayinpast/tarihte bugün topics from $year (e.g. /v1/index/todayinpast/1999).</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/index/olay</td>
		 <td>Returns olan biten.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/message/send</td>
		 <td>Posts a message.This end point uses content-type: application/x-www-form-urlencoded. </td>
		 <td>{'To': RECIPIENT, 'Message': MESSAGE}</td>
		 <td>POST</td>
	  </tr>
	  	  <tr>
		 <td>/v1/message</td>
		 <td>Returns messages.</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
	  <tr>
		 <td>/v1/user/$username</td>
		 <td>Returns $username's profile (e.g. /v1/user/ssg).</td>
		 <td>(optional) add accept-encoding:	gzip to headers.</td>
		 <td>GET</td>
	  </tr>
   </tbody>
</table>

### Status Codes
<table>
	<thead>
		<tr>
			<th>Status Code</th>
			<th>Explanation</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>200</td>
			<td>OK.</td>
		</tr>
		<tr>
			<td>500</td>
			<td>Error in parameters.</td>
		</tr>
		<tr>
			<td>404</td>
			<td>The server didn't find the resource you tried to access.</td>
		</tr>
		<tr>
			<td>503</td>
			<td>Back-end server is at capacity.</td>
		</tr>
	</tbody>
</table>

