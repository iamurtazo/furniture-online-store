"use client";

import { motion } from "framer-motion";
import { Truck, CreditCard, Shield, Clock, CheckCircle, AlertTriangle, Zap, Gift, RefreshCw } from "lucide-react";
import { Header } from "@/components/Header";
import { useStore } from "@/store/useStore";

export default function DeliveryPage() {
    const { user, cart, toggleCart, logout, setSearchQuery } = useStore();
    const cartItemCount = cart.reduce((sum, item) => sum + item.quantity, 0);

    const deliveryOptions = [
        {
            title: "Standard Delivery",
            timeline: "5-7 business days",
            cost: "$15 - $25 (based on location)",
            description: "Perfect for most furniture items",
            icon: Truck,
            color: "bg-blue-500",
        },
        {
            title: "Express Delivery",
            timeline: "2-3 business days",
            cost: "$35 - $50 (based on location)",
            description: "For urgent furniture needs",
            icon: Zap,
            color: "bg-orange-500",
        },
        {
            title: "White Glove Service",
            timeline: "Scheduled appointment",
            cost: "$75 - $150 (based on item size)",
            description: "Includes assembly and placement in your home",
            icon: Gift,
            color: "bg-purple-500",
        },
    ];

    const paymentMethods = [
        {
            category: "Credit Cards",
            methods: ["Visa", "Mastercard", "American Express", "Discover"],
            colors: ["bg-blue-600", "bg-yellow-500", "bg-green-600", "bg-orange-500"],
        },
        {
            category: "Digital Payments",
            methods: ["PayPal", "Apple Pay", "Google Pay"],
            colors: ["bg-blue-700", "bg-gray-800", "bg-red-500"],
        },
    ];

    const deliveryFeatures = ["Delivery to ground floor included", "Two-person delivery team", "Call ahead scheduling", "Additional fees for stairs/elevators"];

    const returnPolicy = ["30-day return window", "Free return pickup", "Full refund on original payment method", "Item must be in original condition"];

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Header */}
            <Header user={user} cartItemCount={cartItemCount} onSearch={setSearchQuery} onLogout={logout} onToggleCart={toggleCart} />

            {/* Hero Section */}
            <div className="bg-gradient-to-r from-gray-900 to-gray-700 text-white py-16">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center">
                        <h1 className="text-4xl md:text-5xl font-bold mb-4">Delivery & Payment</h1>
                        <p className="text-xl text-gray-300 max-w-2xl mx-auto">Convenient delivery options and secure payment methods for your furniture purchase</p>
                    </motion.div>
                </div>
            </div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                {/* Delivery and Payment Options */}
                <div className="grid lg:grid-cols-2 gap-8 mb-12">
                    {/* Delivery Options */}
                    <motion.div initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                        <div className="bg-gray-900 text-white p-6">
                            <div className="flex items-center space-x-3">
                                <Truck size={24} />
                                <h3 className="text-xl font-semibold">Delivery Options</h3>
                            </div>
                        </div>
                        <div className="p-6 space-y-6">
                            {deliveryOptions.map((option, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, y: 10 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ duration: 0.4, delay: 0.1 * index }}
                                    className="border border-gray-200 rounded-lg p-4"
                                >
                                    <div className="flex items-start space-x-4">
                                        <div className={`${option.color} text-white p-3 rounded-lg`}>
                                            <option.icon size={24} />
                                        </div>
                                        <div className="flex-1">
                                            <h4 className="font-semibold text-blue-600 text-lg">{option.title}</h4>
                                            <p className="text-gray-700 mb-1">
                                                <span className="font-medium">Timeline:</span> {option.timeline}
                                            </p>
                                            <p className="text-gray-700 mb-2">
                                                <span className="font-medium">Cost:</span> {option.cost}
                                            </p>
                                            <p className="text-gray-600 text-sm">{option.description}</p>
                                        </div>
                                    </div>
                                </motion.div>
                            ))}

                            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                                <div className="flex items-center space-x-2">
                                    <Gift size={20} className="text-blue-600" />
                                    <span className="font-semibold text-blue-800">Free Delivery</span>
                                    <span className="text-blue-700">on orders over $500!</span>
                                </div>
                            </div>
                        </div>
                    </motion.div>

                    {/* Payment Methods */}
                    <motion.div initial={{ opacity: 0, x: 20 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.6, delay: 0.2 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                        <div className="bg-gray-900 text-white p-6">
                            <div className="flex items-center space-x-3">
                                <CreditCard size={24} />
                                <h3 className="text-xl font-semibold">Payment Methods</h3>
                            </div>
                        </div>
                        <div className="p-6 space-y-6">
                            {paymentMethods.map((category, index) => (
                                <div key={index}>
                                    <h4 className="font-semibold text-green-600 mb-3">{category.category}</h4>
                                    <div className="flex flex-wrap gap-2">
                                        {category.methods.map((method, methodIndex) => (
                                            <span key={methodIndex} className={`${category.colors[methodIndex]} text-white px-3 py-1 rounded-full text-sm font-medium`}>
                                                {method}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            ))}

                            {/* Financing Options */}
                            <div>
                                <h4 className="font-semibold text-green-600 mb-3">Financing Options</h4>
                                <div className="space-y-2">
                                    <p className="text-gray-700">
                                        <span className="font-medium">0% APR</span> for 12 months on purchases over $1000
                                    </p>
                                    <p className="text-gray-700">
                                        <span className="font-medium">Extended Financing</span> up to 24 months available
                                    </p>
                                    <p className="text-gray-600 text-sm">Subject to credit approval</p>
                                </div>
                            </div>

                            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
                                <div className="flex items-center space-x-2">
                                    <Shield size={20} className="text-green-600" />
                                    <span className="font-semibold text-green-800">Secure Checkout</span>
                                </div>
                                <p className="text-green-700 text-sm mt-1">All transactions are encrypted and secure</p>
                            </div>
                        </div>
                    </motion.div>
                </div>

                {/* Important Information */}
                <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.4 }} className="bg-white rounded-xl shadow-lg overflow-hidden">
                    <div className="bg-gray-100 p-6">
                        <div className="flex items-center space-x-3">
                            <AlertTriangle size={24} className="text-gray-700" />
                            <h3 className="text-xl font-semibold text-gray-900">Important Information</h3>
                        </div>
                    </div>
                    <div className="p-6">
                        <div className="grid md:grid-cols-2 gap-8">
                            {/* Delivery Notes */}
                            <div>
                                <h4 className="font-semibold text-gray-900 mb-4 flex items-center space-x-2">
                                    <Truck size={20} className="text-blue-600" />
                                    <span>Delivery Notes</span>
                                </h4>
                                <ul className="space-y-3">
                                    {deliveryFeatures.map((feature, index) => (
                                        <motion.li
                                            key={index}
                                            initial={{ opacity: 0, x: -10 }}
                                            animate={{ opacity: 1, x: 0 }}
                                            transition={{ duration: 0.4, delay: 0.1 * index }}
                                            className="flex items-start space-x-3"
                                        >
                                            {index < 3 ? (
                                                <CheckCircle size={16} className="text-green-500 mt-0.5 flex-shrink-0" />
                                            ) : (
                                                <AlertTriangle size={16} className="text-yellow-500 mt-0.5 flex-shrink-0" />
                                            )}
                                            <span className="text-gray-700">{feature}</span>
                                        </motion.li>
                                    ))}
                                </ul>
                            </div>

                            {/* Return Policy */}
                            <div>
                                <h4 className="font-semibold text-gray-900 mb-4 flex items-center space-x-2">
                                    <RefreshCw size={20} className="text-green-600" />
                                    <span>Return Policy</span>
                                </h4>
                                <ul className="space-y-3">
                                    {returnPolicy.map((policy, index) => (
                                        <motion.li
                                            key={index}
                                            initial={{ opacity: 0, x: -10 }}
                                            animate={{ opacity: 1, x: 0 }}
                                            transition={{ duration: 0.4, delay: 0.1 * index }}
                                            className="flex items-start space-x-3"
                                        >
                                            {index < 3 ? (
                                                <CheckCircle size={16} className="text-green-500 mt-0.5 flex-shrink-0" />
                                            ) : (
                                                <AlertTriangle size={16} className="text-yellow-500 mt-0.5 flex-shrink-0" />
                                            )}
                                            <span className="text-gray-700">{policy}</span>
                                        </motion.li>
                                    ))}
                                </ul>
                            </div>
                        </div>
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
