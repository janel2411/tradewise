import React, { useState } from 'react';
import './App.css';

export default function App() {
    const questions = [
        {
            questionText: 'The forex market allows you to trade ONE currency pair against another currency pair.',
            answerOptions: [
                { answerText: 'True', isCorrect: false },
                { answerText: 'False', isCorrect: true },
            ],
            explanation: 'The forex market allows you to trade multiple currency pairs against each other. If you think one currency will be stronger versus the other, and you end up correct, then you can make a profit.',
        },
        {
            questionText: 'What does it mean to "go long" in forex trading?',
            answerOptions: [
                { answerText: 'Selling a currency pair expecting its value to decrease.', isCorrect: false },
                { answerText: 'Buying a currency pair expecting its value to increase.', isCorrect: true },
                { answerText: 'Selling a currency pair expecting its value to increase.', isCorrect: false },
                { answerText: 'Buying a currency pair expecting its value to decrease.', isCorrect: false },
            ],
            explanation: 'Going long refers to buying a currency against another currency at a lower price with the expectation that its value will increase.',
        },
        {
            questionText: 'What is the worst day of the week to trade?',
            answerOptions: [
                { answerText: 'Monday', isCorrect: true },
                { answerText: 'Tuesday', isCorrect: false },
                { answerText: 'Wednesday', isCorrect: false },
                { answerText: 'Thursday', isCorrect: false },
                { answerText: 'Friday', isCorrect: false },
            ],
            explanation: 'Mondays are typically slower as businesses are coming back from the weekend. Tuesdays to Thursdays are the most productive days for trading.',
        },
        {
            questionText: 'What is the largest financial market in the world?',
            answerOptions: [
                { answerText: 'Stock Market', isCorrect: false },
                { answerText: 'Options Market', isCorrect: false },
                { answerText: 'Forex Market', isCorrect: true },
            ],
            explanation: 'The forex market is the largest and most liquid financial market in the world – larger even than the stock market, with a daily volume of $6.6 trillion.',
        },
        {
            questionText: 'Why is averaging down considered risky in forex trading?',
            answerOptions: [
                { answerText: 'It increases the potential profit of winning trades.', isCorrect: false },
                { answerText: 'It spreads the risk across multiple trades.', isCorrect: false },
                { answerText: 'It reduces the average cost of the positions.', isCorrect: false },
                { answerText: 'It can lead to larger losses by increasing exposure to losing positions.', isCorrect: true },
            ],
            explanation: 'Averaging down increases your exposure to a losing trade. So, it is important to know when to cut your losses and move on.',
        },
    ];


    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [showScore, setShowScore] = useState(false);
    const [score, setScore] = useState(0);
    const [showExplanation, setShowExplanation] = useState(false);
    const [selectedAnswer, setSelectedAnswer] = useState(null);

    const handleAnswerOptionClick = (isCorrect, index) => {
        setSelectedAnswer(index);
        setShowExplanation(true);

        if (isCorrect) {
            setScore(score + 1);
        }
    };

    const handleNextQuestion = () => {
        setShowExplanation(false);
        setSelectedAnswer(null);

        const nextQuestion = currentQuestion + 1;
        if (nextQuestion < questions.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setShowScore(true);
        }
    };

    return (
        <div className="app">
            {showScore ? (
                <div className="score-section">
                    You scored {score} out of {questions.length}
                    <button onClick={() => window.location.href = window.quizHomepageUrl} className="next-quiz-btn">
                        Try Your Next Quiz
                    </button>
                </div>
            ) : (
                <div className="quiz-container">
                    {questions[currentQuestion] && (
                        <>
                            <div className="question-section">
                                <div className="question-count">
                                    <span>Question {currentQuestion + 1}</span>/{questions.length}
                                </div>
                                <div className="question-text">{questions[currentQuestion].questionText}</div>
                            </div>
                            <div className="answer-section">
                                {questions[currentQuestion].answerOptions.map((answerOption, index) => (
                                    <button
                                        key={index}
                                        onClick={() => handleAnswerOptionClick(answerOption.isCorrect, index)}
                                        disabled={showExplanation}
                                        className={
                                            showExplanation && index === selectedAnswer
                                                ? answerOption.isCorrect ? 'correct' : 'incorrect'
                                                : ''
                                        }
                                    >
                                        {answerOption.answerText}
                                    </button>
                                ))}
                            </div>
                            {showExplanation && (
                                <div className="explanation-section">
                                    <p className={questions[currentQuestion].answerOptions[selectedAnswer].isCorrect ? 'correct-text' : 'incorrect-text'}>
                                        {questions[currentQuestion].answerOptions[selectedAnswer].isCorrect
                                            ? 'Correct!'
                                            : 'Incorrect!'}
                                    </p>
                                    <p className="explanation-text">{questions[currentQuestion].explanation}</p>
                                    <button className="next-question-btn" onClick={handleNextQuestion}>
                                        {currentQuestion === questions.length - 1 ? 'View Score' : 'Next Question'}
                                    </button>
                                </div>
                            )}
                        </>
                    )}
                </div>
            )}
        </div>
    );
}
