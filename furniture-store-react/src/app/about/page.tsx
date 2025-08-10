"use client";

import { motion } from "framer-motion";
import { History, Target, Award, TruckIcon, Headphones, CheckCircle, Star, Sparkles, Heart, Shield, Users } from "lucide-react";
import { Header } from "@/components/Header";
import { useStore } from "@/store/useStore";

export default function AboutPage() {
    const { user, cart, toggleCart, logout, setSearchQuery } = useStore();
    const cartItemCount = cart.reduce((sum, item) => sum + item.quantity, 0);

    const stats = [
        { number: "10,000+", label: "Happy Customers", icon: Users, color: "from-blue-500 to-cyan-500" },
        { number: "500+", label: "Furniture Pieces", icon: Sparkles, color: "from-purple-500 to-pink-500" },
        { number: "50+", label: "Cities Served", icon: TruckIcon, color: "from-green-500 to-emerald-500" },
        { number: "7", label: "Years Experience", icon: Award, color: "from-orange-500 to-red-500" },
    ];

    const features = [
        {
            icon: Award,
            title: "Premium Quality",
            description: "Hand-picked furniture from trusted manufacturers with rigorous quality control",
            gradient: "from-blue-500 to-blue-600",
            iconBg: "bg-gradient-to-br from-blue-100 to-blue-200",
            iconColor: "text-blue-600",
        },
        {
            icon: TruckIcon,
            title: "Fast Delivery",
            description: "Quick and reliable delivery service with white-glove assembly options",
            gradient: "from-green-500 to-green-600",
            iconBg: "bg-gradient-to-br from-green-100 to-green-200",
            iconColor: "text-green-600",
        },
        {
            icon: Headphones,
            title: "24/7 Support",
            description: "Dedicated customer service team ready to help with any questions or concerns",
            gradient: "from-purple-500 to-purple-600",
            iconBg: "bg-gradient-to-br from-purple-100 to-purple-200",
            iconColor: "text-purple-600",
        },
    ];

    const missionPoints = [
        {
            icon: Shield,
            title: "Quality First",
            description: "Every piece is carefully selected for durability and craftsmanship",
        },
        {
            icon: Heart,
            title: "Customer Satisfaction",
            description: "Your happiness is our top priority",
        },
        {
            icon: Star,
            title: "Affordable Luxury",
            description: "Premium furniture at prices that won't break the bank",
        },
        {
            icon: Sparkles,
            title: "Sustainable Practices",
            description: "Environmentally responsible sourcing and packaging",
        },
    ];

    const storyTimeline = [
        { year: "2018", title: "Foundation", description: "Started as a small family business with big dreams" },
        { year: "2020", title: "Digital Expansion", description: "Launched our comprehensive online platform" },
        { year: "2022", title: "National Reach", description: "Expanded delivery to 50+ cities nationwide" },
        { year: "2025", title: "Innovation Leader", description: "Leading the industry with cutting-edge solutions" },
    ];

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Header */}
            <Header user={user} cartItemCount={cartItemCount} onSearch={setSearchQuery} onLogout={logout} onToggleCart={toggleCart} />

            {/* Hero Section */}
            <div className="relative bg-gradient-to-br from-slate-900 via-gray-900 to-slate-800 text-white py-24 overflow-hidden">
                {/* Background Pattern */}
                <div className="absolute inset-0 opacity-10">
                    <div className="absolute inset-0 bg-gradient-to-r from-blue-500/20 to-purple-500/20"></div>
                    <div className="absolute top-0 left-0 w-96 h-96 bg-gradient-to-br from-blue-400/30 to-transparent rounded-full blur-3xl"></div>
                    <div className="absolute bottom-0 right-0 w-96 h-96 bg-gradient-to-tl from-purple-400/30 to-transparent rounded-full blur-3xl"></div>
                </div>

                <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8, ease: "easeOut" }} className="text-center">
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            transition={{ duration: 0.8, delay: 0.2 }}
                            className="inline-flex items-center space-x-2 bg-white/10 backdrop-blur-sm px-6 py-3 rounded-full mb-8 border border-white/20"
                        >
                            <Sparkles size={20} className="text-yellow-400" />
                            <span className="text-sm font-medium">Crafting Dreams Since 2018</span>
                        </motion.div>

                        <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">About Our Store</h1>
                        <p className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
                            Discover the story behind our passion for creating
                            <span className="text-blue-400 font-semibold"> beautiful spaces </span>
                            with quality furniture that transforms houses into homes
                        </p>

                        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.6 }} className="mt-12 flex justify-center space-x-8">
                            {["Trusted", "Premium", "Sustainable"].map((badge, index) => (
                                <div key={badge} className="flex items-center space-x-2 text-sm text-gray-400">
                                    <div className="w-2 h-2 bg-gradient-to-r from-blue-400 to-purple-400 rounded-full"></div>
                                    <span>{badge}</span>
                                </div>
                            ))}
                        </motion.div>
                    </motion.div>
                </div>
            </div>

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
                {/* Our Story Timeline */}
                <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="mb-20">
                    <div className="text-center mb-16">
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            transition={{ duration: 0.6, delay: 0.2 }}
                            className="inline-flex items-center space-x-3 mb-6"
                        >
                            <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center">
                                <History size={24} className="text-white" />
                            </div>
                            <h2 className="text-4xl font-bold text-gray-900">Our Journey</h2>
                        </motion.div>
                        <p className="text-xl text-gray-600 max-w-3xl mx-auto">From humble beginnings to industry leadership - discover the milestones that shaped our story</p>
                    </div>

                    {/* Timeline */}
                    <div className="relative">
                        <div className="absolute left-1/2 transform -translate-x-1/2 w-1 h-full bg-gradient-to-b from-blue-500 to-purple-600 rounded-full"></div>
                        <div className="space-y-12">
                            {storyTimeline.map((milestone, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, x: index % 2 === 0 ? -50 : 50 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ duration: 0.6, delay: 0.2 * index }}
                                    className={`flex items-center ${index % 2 === 0 ? "flex-row-reverse" : ""}`}
                                >
                                    <div className={`w-1/2 ${index % 2 === 0 ? "text-right pr-8" : "pl-8"}`}>
                                        <div className="bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transition-shadow border border-gray-100">
                                            <div className="text-2xl font-bold text-transparent bg-gradient-to-r from-blue-500 to-purple-600 bg-clip-text mb-2">{milestone.year}</div>
                                            <h3 className="text-xl font-semibold text-gray-900 mb-2">{milestone.title}</h3>
                                            <p className="text-gray-600">{milestone.description}</p>
                                        </div>
                                    </div>
                                    <div className="relative z-10">
                                        <div className="w-6 h-6 bg-white border-4 border-gradient-to-r from-blue-500 to-purple-600 rounded-full shadow-lg">
                                            <div className="w-full h-full bg-gradient-to-r from-blue-500 to-purple-600 rounded-full"></div>
                                        </div>
                                    </div>
                                    <div className="w-1/2"></div>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </motion.div>

                {/* Our Mission */}
                <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.4 }} className="mb-20">
                    <div className="text-center mb-16">
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            transition={{ duration: 0.6, delay: 0.6 }}
                            className="inline-flex items-center space-x-3 mb-6"
                        >
                            <div className="w-12 h-12 bg-gradient-to-br from-green-500 to-blue-600 rounded-xl flex items-center justify-center">
                                <Target size={24} className="text-white" />
                            </div>
                            <h2 className="text-4xl font-bold text-gray-900">Our Mission</h2>
                        </motion.div>
                        <p className="text-xl text-gray-600 max-w-3xl mx-auto">Guiding principles that drive everything we do</p>
                    </div>

                    <div className="grid md:grid-cols-2 gap-8">
                        {missionPoints.map((point, index) => (
                            <motion.div key={index} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 * index }} className="group">
                                <div className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 transform group-hover:-translate-y-2 border border-gray-100">
                                    <div className="flex items-start space-x-4">
                                        <div className="flex-shrink-0">
                                            <div className="w-14 h-14 bg-gradient-to-br from-gray-100 to-gray-200 rounded-xl flex items-center justify-center group-hover:from-blue-100 group-hover:to-purple-100 transition-all duration-300">
                                                <point.icon size={28} className="text-gray-600 group-hover:text-blue-600 transition-colors duration-300" />
                                            </div>
                                        </div>
                                        <div>
                                            <h3 className="text-xl font-semibold text-gray-900 mb-3 group-hover:text-blue-600 transition-colors duration-300">{point.title}</h3>
                                            <p className="text-gray-600 leading-relaxed">{point.description}</p>
                                        </div>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>

                {/* Why Choose Us */}
                <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.8 }} className="mb-20">
                    <div className="text-center mb-16">
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            transition={{ duration: 0.6, delay: 1.0 }}
                            className="inline-flex items-center space-x-3 mb-6"
                        >
                            <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-600 rounded-xl flex items-center justify-center">
                                <Star size={24} className="text-white" />
                            </div>
                            <h2 className="text-4xl font-bold text-gray-900">Why Choose Us</h2>
                        </motion.div>
                        <p className="text-xl text-gray-600 max-w-3xl mx-auto">We're committed to providing an exceptional furniture shopping experience that exceeds expectations</p>
                    </div>

                    <div className="grid lg:grid-cols-3 gap-8">
                        {features.map((feature, index) => (
                            <motion.div key={index} initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 0.2 * index }} className="group relative">
                                <div className="bg-white p-8 rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300 transform group-hover:-translate-y-3 border border-gray-100 h-full">
                                    {/* Floating Icon */}
                                    <div className="relative mb-6">
                                        <div
                                            className={`${feature.iconBg} w-20 h-20 rounded-2xl flex items-center justify-center mx-auto shadow-lg group-hover:scale-110 transition-transform duration-300`}
                                        >
                                            <feature.icon size={36} className={feature.iconColor} />
                                        </div>
                                        {/* Floating background element */}
                                        <div
                                            className={`absolute -top-2 -right-2 w-6 h-6 bg-gradient-to-r ${feature.gradient} rounded-full opacity-20 group-hover:scale-150 transition-transform duration-300`}
                                        ></div>
                                    </div>

                                    <div className="text-center">
                                        <h3 className="text-2xl font-bold text-gray-900 mb-4 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                                            {feature.title}
                                        </h3>
                                        <p className="text-gray-600 leading-relaxed">{feature.description}</p>
                                    </div>

                                    {/* Gradient border on hover */}
                                    <div
                                        className={`absolute inset-0 rounded-3xl bg-gradient-to-r ${feature.gradient} opacity-0 group-hover:opacity-10 transition-opacity duration-300 pointer-events-none`}
                                    ></div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>

                {/* Statistics */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.8, delay: 1.2 }}
                    className="relative overflow-hidden bg-gradient-to-br from-slate-900 via-gray-900 to-slate-800 rounded-3xl p-12 shadow-2xl"
                >
                    {/* Background Pattern */}
                    <div className="absolute inset-0 opacity-10">
                        <div className="absolute top-0 left-0 w-72 h-72 bg-gradient-to-br from-blue-400/40 to-transparent rounded-full blur-3xl"></div>
                        <div className="absolute bottom-0 right-0 w-72 h-72 bg-gradient-to-tl from-purple-400/40 to-transparent rounded-full blur-3xl"></div>
                    </div>

                    <div className="relative z-10">
                        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6, delay: 1.4 }} className="text-center mb-12">
                            <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">Our Achievements</h2>
                            <p className="text-xl text-gray-300">Numbers that speak to our commitment and success</p>
                        </motion.div>

                        <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
                            {stats.map((stat, index) => (
                                <motion.div
                                    key={index}
                                    initial={{ opacity: 0, scale: 0.5 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    transition={{
                                        duration: 0.6,
                                        delay: 1.6 + 0.1 * index,
                                        type: "spring",
                                        stiffness: 100,
                                    }}
                                    className="text-center group"
                                >
                                    <div className="relative">
                                        {/* Icon with gradient background */}
                                        <div
                                            className={`w-16 h-16 bg-gradient-to-r ${stat.color} rounded-2xl flex items-center justify-center mx-auto mb-4 shadow-lg group-hover:scale-110 transition-transform duration-300`}
                                        >
                                            <stat.icon size={28} className="text-white" />
                                        </div>

                                        {/* Glowing effect */}
                                        <div
                                            className={`absolute inset-0 bg-gradient-to-r ${stat.color} rounded-2xl blur-xl opacity-0 group-hover:opacity-30 transition-opacity duration-300 -z-10`}
                                        ></div>
                                    </div>

                                    <div className={`text-4xl md:text-5xl font-bold bg-gradient-to-r ${stat.color} bg-clip-text text-transparent mb-2`}>{stat.number}</div>
                                    <div className="text-gray-300 font-medium">{stat.label}</div>
                                </motion.div>
                            ))}
                        </div>
                    </div>
                </motion.div>
            </div>

            {/* Footer */}
            <footer className="relative bg-gradient-to-r from-slate-900 to-gray-900 text-white py-16 mt-20">
                <div className="absolute inset-0 opacity-10">
                    <div className="absolute top-0 left-1/4 w-64 h-64 bg-gradient-to-br from-blue-400/30 to-transparent rounded-full blur-2xl"></div>
                    <div className="absolute bottom-0 right-1/4 w-64 h-64 bg-gradient-to-tl from-purple-400/30 to-transparent rounded-full blur-2xl"></div>
                </div>

                <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="text-center">
                        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="mb-8">
                            <div className="inline-flex items-center space-x-3 mb-4">
                                <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                                    <Sparkles size={20} className="text-white" />
                                </div>
                                <span className="text-2xl font-bold">FurnitureStore</span>
                            </div>
                            <p className="text-gray-300 max-w-2xl mx-auto">Transforming houses into homes with premium furniture and exceptional service</p>
                        </motion.div>

                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.6, delay: 0.3 }} className="border-t border-gray-700 pt-8">
                            <p className="text-gray-400">© 2025 FurnitureStore. Built with ❤️ using React, Next.js & Tailwind CSS</p>
                        </motion.div>
                    </div>
                </div>
            </footer>
        </div>
    );
}
