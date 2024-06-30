const express = require('express');
const app = express();
const { MongoClient } = require('mongodb');

const url = 'mongodb+srv://e1156808:OZ9wM6NhvmzElqCO@tradewisecluster.itzxyju.mongodb.net/';
const client = new MongoClient(url);

async function getLeaderboard(req, res) {
    try {
        await client.connect();
        const database = client.db('your_database_name');
        const users = database.collection('users');
        const leaderboard = await users.find().sort({ points: -1 }).limit(3).toArray();
        res.json(leaderboard);
    } finally {
        await client.close();
    }
}

app.get('/api/leaderboard', getLeaderboard);

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
