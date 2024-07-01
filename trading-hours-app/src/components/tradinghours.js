import React, { useEffect, useState } from 'react';
import axios from 'axios';
import moment from 'moment-timezone';
import { Container, Table, FormControl, Select, MenuItem, Typography, Paper } from '@material-ui/core';
import './tradinghours.css';


const TradingHours = () => {
    const [sessions, setSessions] = useState([]);
    const [timezone, setTimezone] = useState(moment.tz.guess());

    useEffect(() => {
        axios.get('/api/sessions/')
            .then(response => {
                setSessions(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the trading sessions!", error);
            });
    }, []);

    const handleTimezoneChange = (event) => {
        setTimezone(event.target.value);
    };

    const formatTime = (time, timezone) => {
        return moment.tz(time, 'HH:mm:ss', timezone).format('h:mm A');
    };

    return (
        <Container>
            <Typography variant="h4" gutterBottom>Trading Hours Tracker</Typography>
            <FormControl variant="outlined" fullWidth margin="normal">
                <Select value={timezone} onChange={handleTimezoneChange}>
                    {moment.tz.names().map(tz => (
                        <MenuItem key={tz} value={tz}>{tz}</MenuItem>
                    ))}
                </Select>
            </FormControl>
            <Paper>
                <Table>
                    <thead>
                        <tr>
                            <th>Market</th>
                            <th>Open Time</th>
                            <th>Close Time</th>
                            <th>Timezone</th>
                        </tr>
                    </thead>
                    <tbody>
                        {sessions.map(session => (
                            <tr key={session.id}>
                                <td>{session.market_name}</td>
                                <td>{formatTime(session.open_time, timezone)}</td>
                                <td>{formatTime(session.close_time, timezone)}</td>
                                <td>{session.timezone}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </Paper>
        </Container>
    );
};

export default TradingHours;
