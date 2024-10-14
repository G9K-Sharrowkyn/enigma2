import React, { useState, useEffect } from 'react';
import CryptoJS from 'crypto-js';
import { LockClosedIcon, LockOpenIcon } from '@heroicons/react/24/solid';
import './App.css';

function App() {
  const [mode, setMode] = useState('select');
  const [keyInput, setKeyInput] = useState('');
  const [keyConfirmed, setKeyConfirmed] = useState(false);
  const [message, setMessage] = useState('');
  const [encryptedMessage, setEncryptedMessage] = useState('');
  const [decryptedMessage, setDecryptedMessage] = useState('');
  const [lettersPerRow, setLettersPerRow] = useState(getLettersPerRow());
  const [topRow, setTopRow] = useState(Array(getLettersPerRow()).fill('A'));
  const [middleRow, setMiddleRow] = useState(Array(getLettersPerRow()).fill(' '));
  const [bottomRow, setBottomRow] = useState(Array(getLettersPerRow()).fill('0'));

  function getLettersPerRow() {
    const width = window.innerWidth;
    if (width < 600) return 4;
    if (width < 900) return 8;
    return 12;
  }

  useEffect(() => {
    const handleResize = () => {
      const newLettersPerRow = getLettersPerRow();
      setLettersPerRow(newLettersPerRow);
      setTopRow(prev => {
        const newRow = [...prev];
        while (newRow.length < newLettersPerRow) newRow.push('A');
        while (newRow.length > newLettersPerRow) newRow.pop();
        return newRow;
      });
      setMiddleRow(prev => {
        const newRow = [...prev];
        while (newRow.length < newLettersPerRow) newRow.push(' ');
        while (newRow.length > newLettersPerRow) newRow.pop();
        return newRow;
      });
      setBottomRow(prev => {
        const newRow = [...prev];
        while (newRow.length < newLettersPerRow) newRow.push('0');
        while (newRow.length > newLettersPerRow) newRow.pop();
        return newRow;
      });
    };

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const shiftChar = (char, direction) => {
    if (/[a-z]/.test(char)) {
      if (direction === 'up') {
        return char === 'z' ? 'a' : String.fromCharCode(char.charCodeAt(0) + 1);
      } else if (direction === 'down') {
        return char === 'a' ? 'z' : String.fromCharCode(char.charCodeAt(0) - 1);
      }
    } else if (/[A-Z]/.test(char)) {
      if (direction === 'up') {
        return char === 'Z' ? 'A' : String.fromCharCode(char.charCodeAt(0) + 1);
      } else if (direction === 'down') {
        return char === 'A' ? 'Z' : String.fromCharCode(char.charCodeAt(0) - 1);
      }
    } else if (/[0-9]/.test(char)) {
      if (direction === 'up') {
        return char === '9' ? '0' : String.fromCharCode(char.charCodeAt(0) + 1);
      } else if (direction === 'down') {
        return char === '0' ? '9' : String.fromCharCode(char.charCodeAt(0) - 1);
      }
    }
    return char;
  };

  const handleConfirmKey = () => {
    if (keyInput.trim() !== '') {
      setKeyConfirmed(true);
    }
  };

  const handleModeSelection = (selectedMode) => {
    setMode(selectedMode);
    setKeyInput('');
    setKeyConfirmed(false);
    setMessage('');
    setEncryptedMessage('');
    setDecryptedMessage('');
    setTopRow(Array(getLettersPerRow()).fill('A'));
    setMiddleRow(Array(getLettersPerRow()).fill(' '));
    setBottomRow(Array(getLettersPerRow()).fill('0'));
  };

  const handleEncryptChange = (e) => {
    const newMessage = e.target.value;
    setMessage(newMessage);

    if (newMessage === '') {
      setEncryptedMessage('');
      setMiddleRow(Array(lettersPerRow).fill(' '));
      setTopRow(Array(lettersPerRow).fill('A'));
      setBottomRow(Array(lettersPerRow).fill('0'));
      return;
    }

    const encrypted = CryptoJS.AES.encrypt(newMessage, keyInput).toString();
    setEncryptedMessage(encrypted);

    const encryptedCharsArray = encrypted.split('');
    setMiddleRow(prev => {
      const shifted = [...prev];
      encryptedCharsArray.forEach(char => {
        shifted.shift();
        shifted.push(char);
      });
      return shifted;
    });
  };

  const handleDecryptChange = (e) => {
    const inputEncryptedMessage = e.target.value;
    setEncryptedMessage(inputEncryptedMessage);

    if (inputEncryptedMessage.trim() === '') {
      setDecryptedMessage('');
      setMiddleRow(Array(lettersPerRow).fill(' '));
      setTopRow(Array(lettersPerRow).fill('A'));
      setBottomRow(Array(lettersPerRow).fill('0'));
      return;
    }

    try {
      const bytes = CryptoJS.AES.decrypt(inputEncryptedMessage, keyInput);
      const decrypted = bytes.toString(CryptoJS.enc.Utf8);
      setDecryptedMessage(decrypted);

      const decryptedCharsArray = decrypted.split('');
      setMiddleRow(prev => {
        const shifted = [...prev];
        decryptedCharsArray.forEach(char => {
          shifted.shift();
          shifted.push(char);
        });
        return shifted;
      });
    } catch (error) {
      console.error('Decryption failed:', error);
      setDecryptedMessage('Błąd podczas deszyfrowania.');
      setMiddleRow(Array(lettersPerRow).fill(' '));
      setTopRow(Array(lettersPerRow).fill('A'));
      setBottomRow(Array(lettersPerRow).fill('0'));
    }
  };

  useEffect(() => {
    const newTopRow = middleRow.map(char => shiftChar(char, 'up'));
    setTopRow(newTopRow);

    const newBottomRow = middleRow.map(char => shiftChar(char, 'down'));
    setBottomRow(newBottomRow);
  }, [middleRow, lettersPerRow]);

  return (
    <div className="enigma-container bg-gray-100 min-h-screen flex flex-col items-center p-4">
      <h1 className="text-4xl font-bold mb-6 text-blue-600">Enigma 2.0</h1>

      {mode === 'select' && (
        <div className="mode-selection flex space-x-6">
          <button
            onClick={() => handleModeSelection('encrypt')}
            className="bg-gradient-to-r from-blue-500 to-blue-700 hover:from-blue-600 hover:to-blue-800 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition transform hover:scale-105 duration-300 flex items-center space-x-2"
          >
            <LockClosedIcon className="h-6 w-6" />
            <span>Szyfruj</span>
          </button>
          <button
            onClick={() => handleModeSelection('decrypt')}
            className="bg-gradient-to-r from-green-500 to-green-700 hover:from-green-600 hover:to-green-800 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition transform hover:scale-105 duration-300 flex items-center space-x-2"
          >
            <LockOpenIcon className="h-6 w-6" />
            <span>Deszyfruj</span>
          </button>
        </div>
      )}

      {mode === 'encrypt' && (
        <>
          {!keyConfirmed ? (
            <div className="input-section flex flex-col items-center space-y-4">
              <input
                type="password"
                placeholder="Klucz szyfrowania"
                value={keyInput}
                onChange={(e) => setKeyInput(e.target.value)}
                className="input-field border border-gray-300 rounded-lg px-4 py-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                onClick={handleConfirmKey}
                className="button bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg shadow transition transform hover:scale-105 duration-300"
              >
                Zatwierdź klucz
              </button>
            </div>
          ) : (
            <div className="input-section flex flex-col items-center space-y-4">
              <input
                type="text"
                placeholder="Wiadomość do zaszyfrowania"
                value={message}
                onChange={handleEncryptChange}
                className="input-field border border-gray-300 rounded-lg px-4 py-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                onClick={() => handleModeSelection('select')}
                className="button bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg shadow transition transform hover:scale-105 duration-300"
              >
                Powrót
              </button>
            </div>
          )}
        </>
      )}

      {mode === 'decrypt' && (
        <>
          {!keyConfirmed ? (
            <div className="input-section flex flex-col items-center space-y-4">
              <input
                type="password"
                placeholder="Klucz deszyfrowania"
                value={keyInput}
                onChange={(e) => setKeyInput(e.target.value)}
                className="input-field border border-gray-300 rounded-lg px-4 py-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-green-500"
              />
              <button
                onClick={handleConfirmKey}
                className="button bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded-lg shadow transition transform hover:scale-105 duration-300"
              >
                Zatwierdź klucz
              </button>
            </div>
          ) : (
            <div className="input-section flex flex-col items-center space-y-4">
              <textarea
                placeholder="Wklej zaszyfrowaną wiadomość"
                value={encryptedMessage}
                onChange={handleDecryptChange}
                className="input-field border border-gray-300 rounded-lg px-4 py-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-green-500"
                rows="4"
              />
              <button
                onClick={() => handleModeSelection('select')}
                className="button bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg shadow transition transform hover:scale-105 duration-300"
              >
                Powrót
              </button>
            </div>
          )}
        </>
      )}

      {(mode === 'encrypt' && keyConfirmed) || (mode === 'decrypt' && keyConfirmed) ? (
        <div className="drums-container flex flex-col items-center mt-8">
          <div className="drum-row flex space-x-2 mb-4">
            {topRow.map((char, index) => (
              <div key={index} className="drum-cell bg-blue-100 border border-blue-300 text-blue-700">
                {char}
              </div>
            ))}
          </div>

          <div className="drum-row flex space-x-2 mb-4">
            {middleRow.map((char, index) => (
              <div key={index} className="drum-cell bg-yellow-300 border border-yellow-500 text-yellow-800">
                {char}
              </div>
            ))}
          </div>

          <div className="drum-row flex space-x-2">
            {bottomRow.map((char, index) => (
              <div key={index} className="drum-cell bg-red-100 border border-red-300 text-red-700">
                {char}
              </div>
            ))}
          </div>
        </div>
      ) : null}

      {mode === 'decrypt' && keyConfirmed && decryptedMessage && (
        <p className="encrypted-message bg-white p-6 rounded-lg shadow mt-6 text-left w-full max-w-2xl">
          <span className="font-semibold text-green-700">Deszyfrowana wiadomość:</span> {decryptedMessage}
        </p>
      )}

      {mode === 'encrypt' && keyConfirmed && encryptedMessage && (
        <p className="encrypted-message bg-white p-6 rounded-lg shadow mt-6 text-left w-full max-w-2xl">
          <span className="font-semibold text-blue-700">Zaszyfrowana wiadomość:</span> {encryptedMessage}
        </p>
      )}
    </div>
  );
}

export default App;
