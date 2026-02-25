const express = require('express');
const router = express.Router();
const Blog = require('../models/Blog');

// Initial seed data from the old static file
const initialBlogs = [
    {
        "title": "ChatGPT, a new artificial intelligence chatbot, has taken the internet by storm",
        "excerpt": "ChatGPT, an advanced artificial intelligence chatbot, has indeed gained significant attention and popularity across the internet.",
        "image": "images/blog_1 (1).webp",
        "category": "Strategy",
        "link": "chatgpt-blog.html",
        "date": "Feb 2024",
        "readTime": "5 min read"
    },
    {
        "title": "Exploring common reasons why many startups often face challenges",
        "excerpt": "Starting a business is an exciting journey, but it's important to be aware of the hurdles that many entrepreneurs face.",
        "image": "images/blog_2 (1).webp",
        "category": "Entrepreneurship",
        "link": "startup-failure-blog.html",
        "date": "Jan 2024",
        "readTime": "6 min read"
    },
    {
        "title": "Fresh perspectives on your business or to discuss a new idea from you",
        "excerpt": "In today's fast-paced world, gaining new perspectives and discussing innovative ideas is crucial for staying ahead in business.",
        "image": "images/blog_3 (1).webp",
        "category": "Innovation",
        "link": "new-age-insights-blog.html",
        "date": "Dec 2023",
        "readTime": "4 min read"
    }
];

// @route   GET /api/blogs
// @desc    Get all blogs
// @access  Public
router.get('/', async (req, res) => {
    try {
        let blogs = await Blog.find().sort({ createdAt: -1 });

        // Auto-seed database if empty (for development/conversion ease)
        if (blogs.length === 0) {
            console.log('Seeding initial blog data to MongoDB...');
            blogs = await Blog.insertMany(initialBlogs);
        }

        res.json({ success: true, count: blogs.length, data: blogs });
    } catch (err) {
        console.error('Error fetching blogs:', err);
        res.status(500).json({ success: false, msg: 'Server Error' });
    }
});

// @route   POST /api/blogs
// @desc    Add a new blog post
// @access  Public (Should be protected in production)
router.post('/', async (req, res) => {
    try {
        const newBlog = new Blog(req.body);
        const savedBlog = await newBlog.save();
        res.status(201).json({ success: true, data: savedBlog });
    } catch (err) {
        console.error('Error adding blog:', err);
        res.status(500).json({ success: false, msg: 'Server Error' });
    }
});

module.exports = router;
