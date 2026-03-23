package com.yizhaoqi.smartpai.utils;

import com.yizhaoqi.smartpai.model.User;
import com.yizhaoqi.smartpai.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.test.util.ReflectionTestUtils;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.lenient;

/**
 * JWT Token刷新机制测试
 */
@ExtendWith(MockitoExtension.class)
public class JwtUtilsRefreshTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private JwtUtils jwtUtils;

    private User testUser;
    private String testSecretKey = "dGVzdC1zZWNyZXQta2V5LWZvci1qd3QtdG9rZW4tZ2VuZXJhdGlvbi1hbmQtdmVyaWZpY2F0aW9u"; // Base64编码

    @BeforeEach
    void setUp() {
        // 设置测试用的密钥
        ReflectionTestUtils.setField(jwtUtils, "secretKeyBase64", testSecretKey);
        
        // 创建测试用户
        testUser = new User();
        testUser.setId(1L);
        testUser.setUsername("testuser");
        testUser.setRole(User.Role.USER);
        testUser.setOrgTags("org1,org2");
        testUser.setPrimaryOrg("org1");

        // Mock用户仓库行为 (使用lenient模式避免不必要的stubbing警告)
        lenient().when(userRepository.findByUsername("testuser")).thenReturn(Optional.of(testUser));
    }

    @Test
    void testGenerateAndValidateToken() {
        // 生成token
        String token = jwtUtils.generateToken("testuser");
        assertNotNull(token);

        // 验证token
        assertTrue(jwtUtils.validateToken(token));

        // 提取用户名
        String username = jwtUtils.extractUsernameFromToken(token);
        assertEquals("testuser", username);
    }

    @Test
    void testShouldRefreshToken() throws InterruptedException {
        // 由于当前REFRESH_THRESHOLD是5分钟，而EXPIRATION_TIME是1小时
        // 正常情况下新生成的token不会触发刷新
        String token = jwtUtils.generateToken("testuser");
        assertFalse(jwtUtils.shouldRefreshToken(token));
        
        // 注意：在实际使用中，当token剩余时间少于5分钟时才会返回true
        // 这里无法模拟等待55分钟，所以这个测试主要验证方法不会抛异常
    }

    @Test
    void testCanRefreshExpiredToken() {
        // 这个方法测试过期token是否能在宽限期内刷新
        // 由于我们无法轻易创建一个刚好过期的token，这里主要测试方法逻辑
        String token = jwtUtils.generateToken("testuser");
        
        // 有效的token不应该被认为是"可刷新的过期token"
        assertFalse(jwtUtils.canRefreshExpiredToken(token));
    }

    @Test
    void testRefreshToken() {
        // 生成原始token
        String originalToken = jwtUtils.generateToken("testuser");
        assertNotNull(originalToken);

        // 刷新token
        String refreshedToken = jwtUtils.refreshToken(originalToken);
        assertNotNull(refreshedToken);

        // 验证刷新后的token
        assertTrue(jwtUtils.validateToken(refreshedToken));

        // 验证用户名仍然正确
        String username = jwtUtils.extractUsernameFromToken(refreshedToken);
        assertEquals("testuser", username);

        // 原始token和刷新后的token应该不同（因为时间戳不同）
        // 注意：由于时间戳精确度的原因，在快速执行时可能会相同，这里添加延迟
        try {
            Thread.sleep(1000); // 等待1秒确保时间戳不同
            String secondRefreshedToken = jwtUtils.refreshToken(originalToken);
            assertNotEquals(originalToken, secondRefreshedToken);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    @Test
    void testRefreshTokenWithInvalidToken() {
        // 测试使用无效token刷新（这个测试不需要mock，因为不会查询数据库）
        String invalidToken = "invalid.token.here";
        String refreshedToken = jwtUtils.refreshToken(invalidToken);
        assertNull(refreshedToken);
    }

    @Test
    void testExtractClaimsFromValidToken() {
        String token = jwtUtils.generateToken("testuser");
        
        // 测试提取各种信息
        String username = jwtUtils.extractUsernameFromToken(token);
        assertEquals("testuser", username);
        
        String role = jwtUtils.extractRoleFromToken(token);
        assertEquals("USER", role);
        
        String orgTags = jwtUtils.extractOrgTagsFromToken(token);
        assertEquals("org1,org2", orgTags);
        
        String primaryOrg = jwtUtils.extractPrimaryOrgFromToken(token);
        assertEquals("org1", primaryOrg);
    }
}