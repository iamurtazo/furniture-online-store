"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Phone, Mail, MapPin, Clock, Send, Facebook, Twitter, Instagram, MessageCircle } from "lucide-react";
import { Header } from "@/components/Header";
import { useStore } from "@/store/useStore";

export default function ContactPage() {
    const { user, cart, toggleCart, logout, setSearchQuery } = useStore();
    const cartItemCount = cart.reduce((sum, item) => sum + item.quantity, 0);

    const [formData, setFormData] = useState({
        name: "",
        email: "",
        phone: "",
        subject: "",
        message: "",
    });

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        alert("Thank you for your message! We'll get back to you soon.");
        setFormData({ name: "", email: "", phone: "", subject: "", message: "" });
    };

    const contactInfo = [
        { icon: MapPin, title: "Our Location", content: ["Furniture Store Headquarters", "123 Furniture Avenue", "Design District, NY 10001", "United States"] },
        { icon: Phone, title: "Phone Numbers", content: ["Customer Service: +1 (234) 567-8900", "Sales Department: +1 (234) 567-8901", "Support: +1 (234) 567-8902"] },
        { icon: Mail, title: "Email Addresses", content: ["info@furniturestore.com", "support@furniturestore.com", "sales@furniturestore.com"] },
    ];

    const businessHours = [
        { day: "Monday - Friday", hours: "9:00 AM - 8:00 PM" },
        { day: "Saturday", hours: "10:00 AM - 6:00 PM" },
        { day: "Sunday", hours: "12:00 PM - 5:00 PM" },
    ];

    const customerService = [
        { service: "Phone Support", availability: "24/7 Available" },
        { service: "Email Response", availability: "Within 2 hours" },
        { service: "Live Chat", availability: "Mon-Fri 9AM-6PM" },
    ];

    const socialLinks = [
        { icon: Facebook, name: "Facebook", color: "bg-blue-600 hover:bg-blue-700" },
        { icon: Twitter, name: "Twitter", color: "bg-sky-500 hover:bg-sky-600" },
        { icon: Instagram, name: "Instagram", color: "bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600" },
    ];

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Header */}
            <Header user={user} cartItemCount={cartItemCount} onSearch={setSearchQuery} onLogout={logout} onToggleCart={toggleCart} />

            {/* Hero Section */}
            <div className="bg-gradient-to-r from-gray-900 to-gray-700 text-white py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center">
                        <h1 className="text-4xl md:text-5xl font-bold mb-4">Contact Information</h1>
                        <p className="text-xl text-gray-300 max-w-2xl mx-auto">Get in touch with us for any questions, support, or feedback</p>
                    </motion.div>
                </div>
            </div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                {/* Contact Details and Business Hours */}
                <div className="grid lg:grid-cols-2 gap-8 mb-12">
                    {/* Contact Details */}
                    <motion.div initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                        <div className="bg-gray-900 text-white p-6">
                            <div className="flex items-center space-x-3">
                                <Phone size={24} />
                                <h3 className="text-xl font-semibold">Get in Touch</h3>
                            </div>
                        </div>
                        <div className="p-6 space-y-6">
                            {contactInfo.map((info, index) => (
                                <div key={index}>
                                    <div className="flex items-center space-x-3 mb-3">
                                        <info.icon size={20} className="text-blue-600" />
                                        <h4 className="font-semibold text-gray-900">{info.title}</h4>
                                    </div>
                                    <div className="ml-8 space-y-1">
                                        {info.content.map((item, itemIndex) => (
                                            <p key={itemIndex} className="text-gray-600">
                                                {item}
                                            </p>
                                        ))}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </motion.div>

                    {/* Business Hours & Support */}
                    <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6, delay: 0.2 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                        <div className="bg-gray-900 text-white p-6">
                            <div className="flex items-center space-x-3">
                                <Clock size={24} />
                                <h3 className="text-xl font-semibold">Business Hours</h3>
                            </div>
                        </div>
                        <div className="p-6 space-y-6">
                            {/* Store Hours */}
                            <div>
                                <h4 className="font-semibold text-green-600 mb-3">Store Hours</h4>
                                <div className="space-y-2">
                                    {businessHours.map((schedule, index) => (
                                        <div key={index} className="flex justify-between">
                                            <span className="font-medium text-gray-700">{schedule.day}:</span>
                                            <span className="text-gray-600">{schedule.hours}</span>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            {/* Customer Service */}
                            <div>
                                <h4 className="font-semibold text-green-600 mb-3">Customer Service</h4>
                                <div className="space-y-2">
                                    {customerService.map((service, index) => (
                                        <div key={index} className="flex justify-between">
                                            <span className="font-medium text-gray-700">{service.service}:</span>
                                            <span className="text-gray-600">{service.availability}</span>
                                        </div>
                                    ))}
                                </div>
                            </div>

                            {/* Social Media */}
                            <div>
                                <h4 className="font-semibold text-green-600 mb-3">Follow Us</h4>
                                <div className="flex space-x-3">
                                    {socialLinks.map((social, index) => (
                                        <motion.button key={index} whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }} className={`${social.color} text-white p-3 rounded-lg transition-colors`}>
                                            <social.icon size={20} />
                                        </motion.button>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </div>

                {/* Contact Form */}
                <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.4 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                    <div className="bg-gray-100 p-6">
                        <div className="flex items-center space-x-3">
                            <Send size={24} className="text-gray-700" />
                            <h3 className="text-xl font-semibold text-gray-900">Send us a Message</h3>
                        </div>
                    </div>
                    <div className="p-6">
                        <form onSubmit={handleSubmit} className="space-y-6">
                            <div className="grid md:grid-cols-2 gap-6">
                                <div>
                                    <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-2">
                                        Full Name *
                                    </label>
                                    <input
                                        type="text"
                                        id="name"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleInputChange}
                                        required
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                    />
                                </div>
                                <div>
                                    <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                                        Email Address *
                                    </label>
                                    <input
                                        type="email"
                                        id="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleInputChange}
                                        required
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                    />
                                </div>
                            </div>

                            <div className="grid md:grid-cols-2 gap-6">
                                <div>
                                    <label htmlFor="phone" className="block text-sm font-medium text-gray-700 mb-2">
                                        Phone Number
                                    </label>
                                    <input
                                        type="tel"
                                        id="phone"
                                        name="phone"
                                        value={formData.phone}
                                        onChange={handleInputChange}
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                    />
                                </div>
                                <div>
                                    <label htmlFor="subject" className="block text-sm font-medium text-gray-700 mb-2">
                                        Subject *
                                    </label>
                                    <select
                                        id="subject"
                                        name="subject"
                                        value={formData.subject}
                                        onChange={handleInputChange}
                                        required
                                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                    >
                                        <option value="">Select a subject...</option>
                                        <option value="general">General Inquiry</option>
                                        <option value="support">Customer Support</option>
                                        <option value="order">Order Question</option>
                                        <option value="delivery">Delivery Issue</option>
                                        <option value="return">Return/Exchange</option>
                                        <option value="other">Other</option>
                                    </select>
                                </div>
                            </div>

                            <div>
                                <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-2">
                                    Message *
                                </label>
                                <textarea
                                    id="message"
                                    name="message"
                                    value={formData.message}
                                    onChange={handleInputChange}
                                    required
                                    rows={5}
                                    placeholder="Please describe your inquiry in detail..."
                                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                                />
                            </div>

                            <div className="text-center">
                                <motion.button
                                    type="submit"
                                    whileHover={{ scale: 1.05 }}
                                    whileTap={{ scale: 0.95 }}
                                    className="bg-gray-900 text-white py-3 px-8 rounded-lg font-semibold hover:bg-gray-800 transition-colors flex items-center space-x-2 mx-auto"
                                >
                                    <Send size={20} />
                                    <span>Send Message</span>
                                </motion.button>
                            </div>
                        </form>
                    </div>
                </motion.div>
            </div>

            {/* Footer */}
            <footer className="bg-gray-900 text-white py-8">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center">
                        <p className="text-gray-300">© 2025 FurnitureStore. Built with React, Next.js & Tailwind CSS</p>
                    </div>
                </div>
            </footer>
        </div>
    );
}
