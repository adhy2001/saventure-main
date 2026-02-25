const express = require('express');
const router = express.Router();
const Contact = require('../models/Contact');

// @route   POST /api/contact
// @desc    Submit a new contact message
// @access  Public
router.post('/', async (req, res) => {
    try {
        const { name, email, subject, message } = req.body;

        // Simple validation
        if (!name || !email || !message) {
            return res.status(400).json({ success: false, msg: 'Please enter all required fields' });
        }

        const newContact = new Contact({
            name,
            email,
            subject,
            message
        });

        const savedContact = await newContact.save();
        res.status(201).json({ success: true, data: savedContact, msg: 'Message sent successfully!' });
    } catch (err) {
        console.error('CRITICAL BACKEND ERROR saving contact:', err);
        res.status(500).json({ success: false, msg: 'Server error. Please try again later.', errorDetails: err.message });
    }
});

module.exports = router;
